import os

#------------类-----------------

class car():
    start_count = 5
    def __init__( self ,types='',lc=0,year='0000'):
        self.name = types
        self.licheng = lc
        self.years = year
        self.speeds=0
    def print_car( self ):    #打印车辆信息
        print('车品牌：'+self.name+ ' 里程数：'+str(self.licheng)+' 生产日期:'+self.years)

    def speed(self):        #速率
        if self.name =='suv':
            self.speeds='时速为：'+'150Km/S'
        elif self.name =='轿车':
            self.speeds= '时速为：' + '120Km/S'
        else:
            self.speeds= '不确定的车型'
        return   self.speeds


    def update_licheng(self,lc):  #里程数更新
        if lc > self.licheng :
            self.licheng = lc
        else:
            print('更新的里程数应比原里程数大！')

    def read_liceng( self ):    #读取里程数
        return self.licheng

    def start( self ):   #车辆启动方法

        while self.start_count>=0 :
            i = input('请输入启动密码：')
            if i == '123':
                start_count = 0
                print('车辆启动成功')
                break
            else:
                self.start_count -=1
                print('启动密码错误：还剩余'+str(self.start_count)+'次')


c = car('aodi',1000,'2017')
c.update_licheng(2300)
c.start()
c.print_car()

class Ecar (car):
    def __init__(self,types):

       # super().__init__(types,lc,year):
        self.name = types

ec = Ecar('bmw')
ec.print_car()

