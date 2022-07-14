# 项目名称

基于Python的豆瓣Top250排行榜影片数据爬取和分析毕业论文+开题报告+答辩PPT+视频讲解+项目源码及运行结果

# 系统介绍
随着互联网的快速发展,在“互联网+”的时态下,大数据的挖掘和分析已成为业界和学术界研究的热点。大数据挖掘可以挖掘先前未知且潜在有用的信息样型或规则，进而转化为有价值的信息或知识，帮助决策者迅速做出适当决策。巧妇难为无米之炊，进行大数据挖掘之前，首先应该获取数据，目前使用Python爬虫技术是使用最广泛的方法之一，可以成功获取互联网上的大数据。为了帮助用户进行影片选择，本文主要基于Python的Scrapy框架，设计并实现对豆瓣电影网上海量影视数据的采集，清洗，保存到本地。并用Pandas，Numpy库对影评进行处理，使用WordCloud对处理的影评进行词云展示，让用户对电影有一个认知。用Matplotlib、Pygal展示口碑+人气电影。

# 环境需要

1.运行环境：最好是java jdk 1.8，我们在这个平台上运行的。其他版本理论上也可以。\
2.IDE环境：IDEA，Eclipse,Myeclipse都可以。推荐IDEA;\
3.tomcat环境：Tomcat 7.x,8.x,9.x版本均可\
4.硬件环境：windows 7/8/10 1G内存以上；或者 Mac OS； \
5.数据库：MySql 5.7版本；\
6.是否Maven项目：否；

# 技术栈

1. 后端：Spring+SpringMVC+Mybatis\
2. 前端：JSP+CSS+JavaScript+jQuery

# 使用说明

1. 使用Navicat或者其它工具，在mysql中创建对应名称的数据库，并导入项目的sql文件；\
2. 使用IDEA/Eclipse/MyEclipse导入项目，Eclipse/MyEclipse导入时，若为maven项目请选择maven;\
若为maven项目，导入成功后请执行maven clean;maven install命令，然后运行；\
3. 将项目中springmvc-servlet.xml配置文件中的数据库配置改为自己的配置;\
4. 运行项目，在浏览器中输入http://localhost:8080/ 登录

# 高清视频演示

https://www.bilibili.com/video/BV1ea411Q7iM/


​