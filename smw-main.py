import requests
import os
import sys
from urllib.parse import quote

BASE_URL = "https://thwiki.cc"
API_URL = "https://thwiki.cc/api.php"
S = requests.session()
requests.adapters.DEFAULT_RETRIES = 5


def get_smw_query(query):
    try:
        response = S.get(API_URL, params={
            "action": "ask",
            "format": "json",
            "query": query,
            "api_version": "2",
            "utf8": 1,
            "formatversion": "2"
        })

        data = response.json()

        file_list = data["query"]["results"]
        if not file_list:
            return []
        return file_list
    except Exception as e:
        print("Query Smw fail", e)
        sys.exit()


def process_input(input_str):
    query = f'{input_str}[[文件:+]]'
    results = get_smw_query(query)
    if not results:
        print("There's no file in the intersection of categories")
        return
    download_image(results)


def download_image(image_list):
    download_path = os.path.join(os.getcwd(), 'Download')
    dir_is_exist = os.path.exists(download_path)
    if not dir_is_exist:
        os.makedirs(download_path)
    for image in image_list:
        split_name = image.split(":", 1)
        if len(split_name) == 1:
            continue
        name = split_name[1]
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


cat_to_process = input('Please input category name need to download image, like [[分类:博丽灵梦]][[分类:东方辉针城]]\n')
process_input(cat_to_process)
