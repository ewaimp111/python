#!/usr/bin/env python3
#代码单元



class Car():

    def __init__(self, chandi,model,year):
        self.chandi = chandi
        self.models =model
        self.year  = year

    def show_info(self):
        print('品牌:'+self.chandi)
        print('型号:'+self.models)
        print('年份:'+str(self.year))

    def usetank(self):
        print('I am is Tanks')

    def read_odo(self):
        return 80

class Eleccar(Car):

    def __init__(self,chandi,model,year):

        self.battery = '99'
        super(Eleccar, self).__init__(chandi,model,year)

    def usetank(self):
        print('I am is Battery')
