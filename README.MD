# Wiki Category Image download
A simple python tool to download images in one category or download
images in category intersection.

## Requirements
just need module [Requests](https://github.com/psf/requests)
```shell script
pip install requests
```
To run this tool, Your mediawiki site need to have [**SemanticMediaWiki**](https://github.com/SemanticMediaWiki/SemanticMediaWiki) installed.

## Run
Run the python file.  
You need to input category name like:
```shell script
[[分类:博丽灵梦]]
```
If you want to get images after category intersection.
Just like:
```shell script
[[分类:东方辉针城]][[分类:博丽灵梦]]
```
Console will status of each file. All files will be saved in `Download` folder.  
If one image file already exist in the folder, and it's size is not zero. This image
will be **skipped**.

## Download Example
![example1](https://a774500050.github.io/img/post-img-wikicatimgdown-exsample3.png)
## About
If you have any problem, just contact [User:SunCL](https://thwiki.cc/User:SunCL).
