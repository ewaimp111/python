#!/usr/bin/env python3

def fun(list1):  #修改列表的函数
    list1.append(1)
    l = set(list1)
    return l

l = [3,2,6,11,3,6,7,3,5]
s = fun(l)
print(s)

def fun1(*param):  #形参的传递及使用

    print(len(param))
    for p in param:
        print('参数分别是： ' + p)

fun1('a','x','y')


def fun2(name,**info):   #传递字典的形参
    dict = {}
    dict['names']=name
    for k,v in info.items():
        dict[k] = v
    return dict

d = fun2('小明',age=12)
print(d)