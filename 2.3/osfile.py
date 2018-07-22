#!/usr/bin/env python3

import os
import random

a=open('t.txt','r')
#print(a.read())
i=0
for n in a:
    i+=1
    #print(str(i)+' '+n.rstrip())
a.close

# 写入文件



s = '878'

print(s[0:7])
print(s[7:10])
print(s[3:-8])

a=open('t.txt','a')
a.write(s+'\n')

a.close


##############

try:
    f=open('t.txt','n')
    f.write('lll')
except ValueError:
    print('x:NameError')
    f.close






