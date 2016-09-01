#!/usr/bin/env python
#coding=utf-8
#author:maohan
#data:20160712
# print [(x+1,y+1) for x in xrange(3) for y in xrange(5)]
import os,sys
import paramiko
import re

t1=paramiko.Transport(('172.16.1.71',22))
t1.connect(username='root',password='haoyi123')
sftp=paramiko.SFTPClient.from_transport(t1)
sftp.get('/var/log/maillog','f://c.log')#下载服务器log
f=open('f://c.log','r')# 打开log
data1=[line.strip() for line in f.readlines()]
print data1
f.close()
t1.close()