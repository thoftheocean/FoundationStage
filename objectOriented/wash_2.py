class Washer:

    def __init__(self, water=15, scour=5):
        self.water = water
        self.scour = scour

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
    #不传递值时，执行默认值
    # w = Washer()
    # w.start_wash()
    #传递值
    wb = Washer(100, 10)
    #用户修改
    wb.set_water(50)
    wb.set_scour(10)

    wb.start_wash()
