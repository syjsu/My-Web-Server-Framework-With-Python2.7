Python Flask项目框架
============

目前线上主站:http://cosplay.applinzi.com/

---

## 概述
>

* 基于flask框架，部署于SAE，七牛SDK，KVDB数据库
* 主要目录结构为

~~~

--index.wsgi        # SAE线上使用的主程序入口
--dev_server.py     # PyCharm本地调试的主程序入口

--docs              # 和Readme.md相关的说明文档
--virtualenv.bundle # 纯Python的代码包,用于SAE之类云环境没有相关库文件而主动添加上去
--static            # 静态库文件,比如bootstrarp\jQuery之类

--Application

    --view          # 路由,处理各种http请求
    --templates     # 模板路径,供给路由渲染
    
    --public        # 公开类处理工具 杂物等(不符合MVC模式的一些杂项代码)
    --protected     # 自定义数据模型model 控制器controller (基本自己写的)
    --private       # 全局公用的一些方法等(写好的轮子,建议别动)

~~~


![预览图1](/docs/截图1.png)
![预览图2](/docs/截图2.png)

---

## 功能简介
* 七牛JS-SDK基本功能：上传，预览，水印，旋转，缩放等（部分已被隐藏）
* 按上传时间倒序，瀑布流布局，自动加载更多
* 长图底部波浪线，隐藏超出部分
* 封装sae的KVDB方便调用

---

## 安装和运行
* 本地调试直接运行dev_sever.py
* 在线运行直接调用index.wsgi

---
## 修改历史
* 2016-07-15：第一次规划该框架

## 说明
1. flask相关可直接看[flask快速上手](http://dormousehole.readthedocs.org/en/latest/quickstart.html#)
2. 七牛上传仔细查阅[七牛Python官方文档](http://developer.qiniu.com/docs/v6/sdk/python-sdk.html)
