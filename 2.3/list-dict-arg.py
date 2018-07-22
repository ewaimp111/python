#!/usr/bin/env python3



import  random

ds = {'a':1,'b':2,'c':4}
def test(**d):
    td = dict(d)
    for k in td.keys():
        if k =='a':
            td[k]=66
        else:
            td[k]=0
    print(td)
    return td

#print(test(ds))
test(**ds)


ls = [1,3,4]
def tuples(a):
    for i in list(a):
        a.append(i*2)
        a.insert(len(a)-1,i*3)
    return a
tuples(ls)
print(ls)

def returnval(*l):  #返回多个值
    tmp =[]
    sum = 0
    for i in l:
        sum +=i
        tmp.append(i*2)
    if sum>10:
        bool=True
    else:
        bool=False
    return tmp,sum

l =[2,40]
b = 0
b,l = returnval(b,*l)

print(l,b)








