#!/usr/bin/env python
#coding=utf8
#抓取百度歌曲名单
import urllib2,re,sys,os,time
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')

def musicScapy(singername):
	query=urllib2.quote(singername)
	url='http://music.baidu.com/search?key='+query
	page=urllib2.urlopen(url)
	response=page.read()
	mysoup=BeautifulSoup(response,"html.parser")
	guolv=mysoup.find_all('span',class_="song-title")#查找歌曲标签
	if (os.path.exists('songs')==False):#建立歌曲目录和歌词目录
		os.mkdir('songs')
	if (os.path.exists('lrcs')==False):
		os.mkdir('lrcs')
	pagesize=len(guolv) #显示数
	for i in xrange(0,pagesize):
		print  guolv[i].a.get_text()#获取歌曲名称
musicScapy('张国荣')