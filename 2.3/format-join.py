#!/usr/bin/env python3
import pprint

import itertools




name = 'jack'
age =30
jbo = 'cto'
saler = 11234.24532
phone =['15219821926','18124890912']

#第一个格式化
ss = '姓名:{0:>30}    ' \
     '\n年龄:{1:>30}  ' \
     '\n联系电话:{2}   ' \
     ' \n工资:{3:>30.2f}'.format(name,age,phone,saler)
# {}中：左边是参数序号，右边是格式化符号，工资这个参数是指向右对齐30个空格，长度为10，精度为2

print(ss)

print('{:^030}'.format('居中对其，末尾自动换行'))


#------------------------join--------------------
f=34.23234342
l1 = ['how','are','you']
s1 = '圆周率为：%10.4f' % (f)

print(s1)

r=' '.join(l1)
print(r[:6])

#--------------------spilt---------------

s = 'a,b,c,d,e,a,b,c'
print(s.split())
print(s.split('a',4))

us= '-A-B-C-'
xs=us.lower()
if xs.islower():
    print('is lower')
else:
    print('is Upper')
xs.strip('-')

aa ='-kjk-kjks-'
print(aa.strip('-'))
print(aa.rstrip('-'))


