import requests
import os
import sys
from urllib.parse import quote

BASE_URL = "https://thwiki.cc"
API_URL = "https://thwiki.cc/api.php"
S = requests.session()
requests.adapters.DEFAULT_RETRIES = 5


def retrieve_csrf_token():
    """retrieve Csrf token after login"""
    try:
        response = S.get(url=API_URL, params={
            "action": "query",
            "meta": "tokens",
            "format": "json"
        })

        data = response.json()

        csrftoken = data["query"]["tokens"]["csrftoken"]
        return csrftoken
    except Exception as e:
        print(f'Error while retrieve csrftoken:{e}, try run the program again')
        sys.exit()


def read_bot_token():
    """
    using local token file, you need to make a BotToken.txt file
    the token file should like
    """

    """
        botusername=XXXXX
        botpassword=XXXXX
    """
    token_exist = os.path.isfile("BotToken.txt")
    if not token_exist:
        print(f'You need to have a BotToken.txt in the current directory for high-volume editing')
        sys.exit()

    f = open(r"BotToken.txt", "r", encoding="utf-8")

    bot_token = {}

    for line in f.readlines():
        name, value = line.strip("\n").split("=", 1)
        bot_token[name] = value
    return bot_token


def fetch_login_token():
    """ Fetch login token via `tokens` module """

    response = S.get(
        url=API_URL,
        params={
            'action': "query",
            'meta': "tokens",
            'type': "login",
            'format': "json"})
    data = response.json()
    return data['query']['tokens']['logintoken']


def start_bot_login(botusername, botpassword):
    """using BotPasswords to login with API access"""

    login_token = fetch_login_token()

    response = S.post(url=API_URL, data={
        "action": "login",
        "lgname": botusername,
        "lgpassword": botpassword,
        "lgtoken": login_token,
        "format": "json"
    })

    data = response.json()

    if data['login']['result'] == 'Success':
        print("Login Success")
    else:
        print("Login Failed")


def get_cat_file_st(cat_name):
    cat_file_set = set()

    response = S.get(url=API_URL, params={
        "action": "query",
        "format": "json",
        "prop": "info",
        "generator": "categorymembers",
        "utf8": 1,
        "formatversion": "2",
        "gcmtitle": cat_name,
        "gcmprop": "title",
        "gcmnamespace": "6",
        "gcmtype": "file",
        "gcmlimit": "max"
    })

    data = response.json()
    if not data["batchcomplete"]:
        print("query category info failed")
        sys.exit()
    if "query" not in data:
        print(f"{cat_name} has no file")
        return cat_file_set
    pages_data = data["query"]["pages"]
    for page in pages_data:
        title = page['title']
        cat_file_set.add(title)
    return cat_file_set


def process_input(input_str):
    cat_name_list = input_str.split("|")
    intersected_set = set()
    flag = True
    for cat_name in cat_name_list:
        if "分类" not in cat_name:
            continue
        cat_file_set = get_cat_file_st(cat_name)
        if cat_file_set:
            if flag:
                intersected_set = cat_file_set
                flag = False
            else:
                intersected_set.intersection_update(cat_file_set)
    if intersected_set:
        download_intersected_image(intersected_set)
    else:
        print("There's no file in the intersection of categories")


def download_intersected_image(image_set):
    download_path = os.path.join(os.getcwd(), 'Download')
    dir_is_exist = os.path.exists(download_path)
    if not dir_is_exist:
        os.makedirs(download_path)
    for image in image_set:
        name = image[3:]
        formed_image_query = f'/{quote("特殊:重定向")}/?wptype=file&wpvalue={quote(name)}'
        image_path = os.path.join(download_path, name)
        if os.path.exists(image_path) and (os.path.getsize(image_path) != 0):
            continue
        else:
            try:
                response = S.get(BASE_URL + formed_image_query)
                with open(image_path, 'wb') as f:
                    f.write(response.content)
                    print(f"Download {name} Success")
            except Exception as e:
                print(f"Download {name} fail", e)


# file_list = ['东方三月精V3卷封面.jpg', '东方三月精V连载第一话封面.jpg', '东方三月精V第一卷通常版cover2.jpg']
# path = os.path.join(os.getcwd(), 'Download')
# dir_is_exist = os.path.exists(path)
# if not dir_is_exist:
#     os.makedirs(path)
# os.chdir(path)
# for file in file_list:
#     formed_image_query = f'/{quote("特殊:重定向")}/?wptype=file&wpvalue={quote(file)}'
#     r = S.get(BASE_URL+formed_image_query)
#     with open(file, 'wb') as f:
#         f.write(r.content)


BOT_TOKEN = read_bot_token()
start_bot_login(BOT_TOKEN["botusername"], BOT_TOKEN["botpassword"])
CSRF_TOKEN = retrieve_csrf_token()

# a = get_cat_file_st("分类:博丽灵梦")

cat_to_process = input('Please input category name need to download image, if multi cat use " | " as separator:\n')
process_input(cat_to_process)
