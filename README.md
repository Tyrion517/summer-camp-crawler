# summer-camp-crawler
获取各大高校的夏令营信息并集合在一个网站。后端

## 食用方式

运行server.py

1. 使用curl

   例如 curl.exe 127.0.0.1:8000/ustc

2. 结合前端，以网页的形式食用

## 添加学校的方式

共需修改两处：

1. 将相关信息输入/data/meta.json
2. 在server.py中添加新的controller函数

