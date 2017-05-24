class Washer:
    company = 'lexi'

    def __init__(self, water=15, scour=5):
        self._water = water
        self.scour = scour
        self.year = 2010

    #静态方法
    @staticmethod
    def spins_m1(spains):
        print('company:', Washer.company)  #静态方法中可以直接引用类的属性
        return spains*0.4

    #属性包装
    @property
    def water(self):
        return self._water

    @water.setter
    def water(self, water):
        if 0 < water <= 500:
            self._water = water
        else:
            print('设置失败')
    @property
    def total_year(self):
        return 2015-self.year



    def set_water(self, water):
        self.water = water

    def set_scour(self, scour):
        self.scour = scour

    def add_water(self):
        print('Add water', self.water)

    def add_scour(self):
        print('Add scour', self.scour)

    def start_wash(self):
        self.add_water()
        self.add_scour()
        print('start wash...')

if __name__ =='__main__':
    # w = Washer()
    # print(w.water)
    # w._water = 400
    # w.water = 600
    # # print(w.water)
    #
    # w.set_water(50)
    # w.start_wash()
    # print(w.year)
    # print('洗衣机已经使用了', w.total_year)

    #静态方法
    print(Washer.spins_m1(8)) #利用类直接调用静态方法
    w = Washer()
    print(w.spins_m1(8)) #利用类实例直接调用静态方法
    w = Washer(200, Washer.spins_m1(9))
    w.start_wash()