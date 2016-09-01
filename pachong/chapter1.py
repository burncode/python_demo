#!/usr/bin/env python
#coding=utf8
#author:burncode
#date:20160901
#decription:爬虫demo第一章
#version:0.1
import urllib2
from bs4 import BeautifulSoup
response=urllib2.urlopen("http://pythonscraping.com/pages/page1.html");#请求http数据
Mybs=BeautifulSoup(response.read(),"html.parser")#读取数据并放入到beautifulsoup容器中
print(Mybs)#打印返回的所有数据
print(Mybs.head)#打印<head>标签包裹的数据
print(Mybs.head.title)#打印<head>标签下title标签数据
print(Mybs.head.title.text)#打印title标签中的内容