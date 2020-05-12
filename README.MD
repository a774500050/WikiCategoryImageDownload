# Wiki Category Image download
A simple tool to download images in one category or download
images in category intersection.  
Check out [**smw-version**](https://github.com/a774500050/WikiCategoryImageDownload/tree/smw-version) branch if your 
wiki has  [**SemanticMediaWiki**](https://github.com/SemanticMediaWiki/SemanticMediaWiki) installed.
## Attention
This tool has been modified to [**THBWiki**](https://thwiki.cc), you need to change the **`BASE_API`** and
**`API_URL`** parameter to your wiki's path.
## Requirements
just need module [Requests](https://github.com/psf/requests)
```shell script
pip install requests
```

## Start
Since images in one category may be over 500
> cmlimit  
> The maximum number of pages to return.   
> No more than 500 (5000 for bots) allowed. Enter max to use the maximum limit.

You need to create a [BotPassword](https://thwiki.cc/Special:BotPasswords).
>Bot passwords allow access to a user account via the
> API without using the account's main login credentials.
> The user rights available when logged in with a bot password may be restricted.

You will need at least those permissions:
* Basic rights (granted default 基本权限 默认已授权)
* Create, edit, and move pages (High-volume editing 大容量编辑)

After creating the bot, just create a **BotToken.txt** in the **main.py** file's
same directory.  
The **BotToken.txt** file should be encoded in UTF-8 and like this:
```text
botusername=XXXXX
botpassword=XXXXX
```
Then you can run the python file.

## Run
Run the python file.  
If you set the bot correctly, you will see the terminal shows:
```shell script
Login Success
```
Then you need to input category name  
For example:
```shell script
分类:博丽灵梦
```
If you want to get images after category intersection.
Categories you input should be separate by `|`(Vertical bar U+007C)  
For example:
```shell script
分类:东方辉针城|分类:少名针妙丸
```
Console will show status of each file. All files will be saved to `Download` folder.  
If one image file already exist in the folder, and it's size is not zero. This image
will be **skipped**.

## Download Example
Download with same file failed:
![example1](https://a774500050.github.io/img/post-img-wikicatimgdown-exsample1.jpg)
Run the tool again, and continue to download:
![example2](https://a774500050.github.io/img/post-img-wikicatimgdown-exsample2.png)
## About
If you have any problem, just contact [User:SunCL](https://thwiki.cc/User:SunCL).