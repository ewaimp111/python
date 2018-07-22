#!/usr/bin/env python3

infos = {
    'name':'haozi',
    'age':'22',
    'language':['english','chinese']
}


for n,l in infos.items():
    print('\n'+n)
    for lg in l:
        print('\t'+lg)
print(infos['language'][1])

actives = True
while  actives:
    num = input('请输入一个数字编号：')
    if not num.isdigit():
        print('no invable of string')
        break
    elif int(num) == 1 :
        print('help')

    elif int(num) == 2 :
        print('usergui')
    elif int(num) == 0:
        print('progream quit!')
        active =False
        break
    else:
        print('no find case')

     ##------------验证信息-------------

ok_user=[]

unok_user=['aric','aoli','johe']

while unok_user:
    curr_user = unok_user.pop()
    print('curr_user:'+curr_user)
    ok_user.append(curr_user)

print(ok_user)



