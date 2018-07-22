#!/usr/bin/env python3

from collections import  namedtuple
from collections import  deque

point = namedtuple('po',['x','y','z'])  #通过元祖命名显示坐标

Ssc = namedtuple('ssc',['caizhong','shangqi','xiaqi','number'])
Ssc.caizhong='天津时时彩'
Ssc.shangqi='023'
Ssc.xiaqi='024'
Ssc.number='24223'         #绑定参数为记录形式

print(Ssc.caizhong,Ssc.shangqi,Ssc.xiaqi,Ssc.number)

ssc =Ssc('北京时时彩','002','003','34223')

print(*ssc , ssc.caizhong)

#------------------deque
ll= [1,3,2]

de = deque(ll)  #增强列表的速度型
de.appendleft(0)
de.append(1)
print(de)
de.remove(1)
print(*de)



#------------------lambda---------------
#类似于匿名函数，左边参数，右边计算返回的表达式
my = lambda arg ,arg1: arg * arg1 +100
print(my(10,20))

x = (lambda x1 = 'a', x2 = 'b': x1 + x2 )
print(x('11','22'))
print('\n')
l = [lambda s1 : s1 ** 2,
     lambda s2 : s2 ** 3,
     lambda s3 : s3 ** 4]

for i in l:
    print(i(4))
print(l[0](3))

l=[3,5,7,8,9,33]

x = (lambda i:i in l )  #34是否包含在列表l里面，结果返回bool
print(x(34),end='\n')

#-----------------filter--------------
#filter()函数用于过滤序列，左边计算的函数，右边序列参数

def isodd(n):
    return  n % 3 == 0

fl = list(filter(lambda x:x % 3 == 0,[3,4,5,6,7,8,9]))
print(fl)
fl = list(filter(isodd,[3,6,8,9,12]))
print(fl)

#----------------itrtools.permutations--------------
import itertools as it
li=list(it.combinations('牛马猪羊',3))
print(li)
print(len(li))
