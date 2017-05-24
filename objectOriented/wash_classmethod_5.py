class Washer:
    company = 'lexi'

    def __init__(self, water=15, scour=5):
        self._water = water
        self.scour = scour
        self.year = 2010

    #静态方法
    @staticmethod
    def spins_m1(spains):
        return spains*0.4  #将勺转化为升

    #类方法
    @classmethod
    def get_washer(cls, washer, scour):
        print('company:', Washer.company)  # 类方法中可以直接引用类的属性
        return cls(washer, cls.spins_m1(scour))


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

if __name__ == '__main__':
    w = Washer.get_washer(100, 9)  # 类直接调用类方法
    w.start_wash()

    b = Washer
    c = b.get_washer(100, 9)
    c.start_wash()




