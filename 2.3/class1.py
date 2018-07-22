#!/usr/bin/env python3

import time  as t

import datetime as dt

tt = t.strftime('%Y-%m-%d %X',t.localtime())
print(tt)

d1=dt.time(10,00,00)



cptypes = ('时时彩','北京PK10','11选5','分分彩')

class CaiPiao():
    def __init__(self,name):
        self._name = name

    def showinfo(self):
        print('当前彩票:'+self._name)

    def is_stop(self):
        return true

class CQssc(CaiPiao):
    def __init__(self,name,qishu):
        super(CQssc, self).__init__(name)
        self._qishu = qishu

    def showqishu(self):
        print('当前期数:',str(self._qishu))

    def setsize(self,size):
        self._height,self._width = size

    def getsize(self):
        return self._width,self._height



cqssc = CQssc('重庆时时彩',120)
cqssc.showinfo()
cqssc.showqishu()

jxssc = CQssc('江西时时彩',100)
jxssc.showinfo()
jxssc.showqishu()
jxssc.setsize((111,222))
x= jxssc.getsize()
print(x)


__metaclass__ = type
class A():
    def __init__(self):
        self._width = 0
        self._height =0

    def getsize(self):
        return self._height,self._width

    def setsize(self,size):
        self._height,self._width=size

    size = property (getsize,setsize)


a = A()
a._height =11
a._width =22

print('a',a.getsize())


class B():
    def __init__(self):
        self.name=''

    @staticmethod
    def hello(self,name):  #静态方法有self参数，调用时参数设置类名
        print('i am is staticmoth',name)
        self.name=name

    def printname(self):
        print(self.name)

B.hello(B,'abc')
B.printname(B)



class C():
    def __init__(self):
        pass

    def call(a):
        print('call test',a)

    @staticmethod   #静态方法不用参数self ，可以添加其他参数
    def smoth(n):
        print('this is a static moth',n)

    @classmethod    #同静态方法一样，不用实例化,可以直接调用类中方法
    def cmoth(cls):
        print('this is a class moth',cls)
        C.call('')



C.smoth('C')
C.cmoth()
C.call('me')


