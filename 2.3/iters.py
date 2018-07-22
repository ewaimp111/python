#!/usr/bin/env python3

#迭代器的使用

import sys
import os

l = [ x * x for x in range(1,10) if x % 2 == 0]
print(l)

dir=[d for d in os.listdir('.') ]
for d in dir :
    print(d)

nums = {'a':'abc','b':'bcd'}
num = [k +'='+ v for k,v in nums.items() if k != 'a']
print(num)


L = ['Hello', 'World', 'IBM', 43,44.222,'Apple']
l = [s.lower() for s in L if isinstance(s,str)]
print(l)

s ='aaa'
i = 22
f = 2.222
n = None

b = isinstance(i,str)
print(b)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
       // print(b)
       yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
print(fib(6))
