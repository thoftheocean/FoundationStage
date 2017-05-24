class Washer:

    def __init__(self, water=15, scour=5):
        self._water = water
        self.scour = scour
        self.year = 2010

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
    w = Washer()
    print(w.water)
    w._water = 400
    w.water = 600
    # print(w.water)

    w.set_water(50)
    w.start_wash()
    print(w.year)
    print('洗衣机已经使用了', w.total_year)
