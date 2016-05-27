#!/usr/bin/env python
#coding=utf-8
#列表学习
#Date:20160527
Date=['rsd','bbds','ccasd','fsad']
def Compare(a='',b=''):
	len_a=len(a);
	len_b=len(b);
	Long=min(len_a,len_b)
	i=0
	while i<Long:
		if a[i]<b[i]:
			return -1
		elif a[i]>b[i]:
			return 1
		i=i+1
	return -1
Date=sorted(Date,cmp=Compare)
print Date
Date.insert(4,[1,2,3,4,5,6])
print Date