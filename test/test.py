#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import arrow
import faker
import time
import py2app

def main():
    b= input('输入密码：')
    a = arrow.now()
    print(a.date(),a.time())
    f = faker.Faker(locale='zh-cn')
    print(f.name(),f.address())
    time.sleep(3)

if __name__ == '__main__':
    main()






