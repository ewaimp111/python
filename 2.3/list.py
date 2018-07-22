#!/usr/bin/env python3
import  os
import numpy as np

#列表操作
l =['a','c','b','b','c','f']

s = set(l) #去除所有重复项
print(s)

while 'c' in l :
    l.remove('c')   #去除指定字符重复项
print(l)


yazhou_country =['中国','日本','韩国']
countrys = ['中国', '德国', '法国', '日本', '韩国']
fool_pop = []

print(countrys[1:]) #从第一个到最后所有元素
print(countrys[:-1]) #访问最后一个元素

countrys[2] = '意大利' #修改元素
countrys.append('美国')  #添加元素
countrys.insert(-1, '印度')  #插入元素
#del (fool[1])   #删除元素
fool_pop=countrys.pop()   #从列表尾部删除元素
#fool.remove('orgren') # 根据值删除元素
countrys.sort()  #列表永久排序

print(countrys)

countrys.reverse()  #列表反转排序
print(countrys)
print('列表的长度是：' + str(len(countrys)))

###########################################

a=[i in yazhou_country for i  in countrys]
n=0
for t in a:
    if t:print(countrys[n])
    n += 1

l2 = [3,42,12,50,1,3]
print(max(l2)) #最大数

l3 = l2[:]  #切片赋值后两个列表添加数据均独立

print(l2)

l3.append(0)

print(l3)








