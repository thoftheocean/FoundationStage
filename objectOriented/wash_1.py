class Washer:

    def __init__(self):
        # 初始化，标准水和洗涤剂量
        self.water = 15
        self.scour = 3

    #设置水量
    def set_water(self, water):
        self.water = water
    #设置洗涤剂量
    def set_scour(self, scour):
        self.scour = scour

    def add_water(self):
        print('Add water', self.water)

    def add_scour(self):
        print('Add scour', self.scour)

    def start_wash(self):
        self.add_water()   #调用类内方法
        self.add_scour()
        print('start wash...')

if __name__ == '__main__':
    w = Washer()
    w.set_water(10)
    w.set_scour(5)
    w.start_wash()