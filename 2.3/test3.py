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

