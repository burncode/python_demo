#!/usr/bin/env python
#coding=utf-8
#author:maohan
#date:20160706
#decription:通过百度api获取相关信息，并保存为xls格式
#ver:1.0
import urllib2
import json
import sys
from pyExcelerator import *
def bd_finder(qw,region,page_num):
	page_size='20'
	bd_ak='wkEmrv7B1l0KPpi30F1G2VMx10xEdeol'
	bd_url='http://api.map.baidu.com/place/v2/search?'
	furl=bd_url+'q='+qw+'&page_size='+page_size+'&page_num='+page_num+'&region='+region+'&output=json&ak='+bd_ak
	page = urllib2.urlopen(furl)
	html=page.read()
	data=json.loads(html)
	w=Workbook()
	ws=w.add_sheet('test')
	str1='医院名称'
	str2='医院地址'
	str3='电话号码'
	str4='维度'
	str5='经度'
	ws.write(0,0,str1.decode('utf-8'))
	ws.write(0,1,str2.decode('utf-8'))
	ws.write(0,2,str3.decode('utf-8'))
	ws.write(0,3,str4.decode('utf-8'))
	ws.write(0,4,str5.decode('utf-8'))
	# print type(data['results'])
	# print len(data['results'])
	count=0
	for i in data['results']:
		# print("名称:%-35s")  %(i.get('name'))
		# print("-------地址:%-35s")  %(i.get('address'))
		# print("-------电话:%-35s")  %(i.get('telephone'))
		# print("-------定位:(维度:%-10s)(经度:%-10s)") %(i.get('location')['lat'],i.get('location')['lng'])
		# print (format("","100"))
		count+=1
		ws.write(count,0,'%s' %(i.get('name')))
		ws.write(count,1,'%s' %(i.get('address')))
		ws.write(count,2,'%s' %(i.get('telephone')))
		ws.write(count,3,'%s' %(i.get('location')['lat']))
		ws.write(count,4,'%s' %(i.get('location')['lng']))
	w.save('test.xls')
for k in xrange(0,10):
	bd_finder('医院','武汉',str(k))

	