#!/usr/bin/env python3

weeks =('星期一','星期二','星期三','星期四','星期五','星期六','星期天')
print(weeks)
xiuxi_week=['星期六','星期天']

for week in weeks:
    if week in xiuxi_week:
        print('非工作日:'+week)
    else:
        print('正常工作')

#在职人员信息

infos = {'姓名':'刘浩','部门':'楼面部','职位':'店长','年龄':'22'}
infos['phone']='13202023333'
for key,val in infos.items():
    print(key+':'+val)


l = {6:2,5:2,2:44,7:1}

for k,v in sorted(l.items()):  #遍历列表中的键和值
    print(str(k)+' '+str(v))

test =['c','go','delphi','c','python','c']

s = set(sorted(l))  #字典转换为列表并排序
print(s)

print(test.count('c'))







