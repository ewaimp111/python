#!/usr/bin/env python3


class Testclass():
    initcount = 0


    def __init__(self):
        Testclass.initcount+=1
        self.__checked__ = False


    def check(self,ok):
        self.__checked__ = ok
        return ok


    def start(self):
        if self.__checked__:
            print('指令检查成功，机器已启动')
        else:
            print('指令未成功，启动失败')

    @classmethod
    def test(self):
        print('test')

t1 = Testclass()
t1.check(True)
t1.start()

Testclass.test(d∂)



t2 = Testclass()
t2.start()

print(str(t1.initcount))

