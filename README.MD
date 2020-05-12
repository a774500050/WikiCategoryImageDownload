# Wiki Category Image download
A simple python tool to download images in one category or download
images in category intersection.

Check out [**master**](https://github.com/a774500050/WikiCategoryImageDownload) branch if your 
wiki **doesn't** have [**SemanticMediaWiki**](https://github.com/SemanticMediaWiki/SemanticMediaWiki) installed.

## Attention
This tool has been modified to [**THBWiki**](https://thwiki.cc), you need to change the **`BASE_API`** and
**`API_URL`** parameter to your wiki's path.  
To run this tool, your MediaWiki site need to have [**SemanticMediaWiki**](https://github.com/SemanticMediaWiki/SemanticMediaWiki) installed.

## Requirements
just need module [Requests](https://github.com/psf/requests)
```shell script
pip install requests
```

## Run
Run the python file `smw-main.py`.  
You need to input category name like:
```shell script
[[分类:博丽灵梦]]
```
If you want to get images after category intersection.
Just like:
```shell script
[[分类:东方辉针城]][[分类:博丽灵梦]]
```
Console will show status of each file. All files will be saved in `Download` folder.  
If one image file already exists in the folder, and it's size is not zero. This image
will be **skipped**.

## Download Example
![example1](https://a774500050.github.io/img/post-img-wikicatimgdown-exsample3.png)
## About
If you have any problem, just contact [User:SunCL](https://thwiki.cc/User:SunCL).
