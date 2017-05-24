# !/usr/bin/env python
# coding:utf-8
# author:hx

'''
定义一个类Box，具有实例属性长度（length）、宽度（width）、高度（height）。
具有私有属性体积（由长、宽、高计算得来），并且它的每个实例可以知道它被实
例化的数量。然后实例化它们五次，并输出每个实例的所有属性。
'''

class Box:
    def __init__(self):
        self.length = 10
        self.width = 5
        self.height = 8
        self._volume = 0

    def info(self):
        self._volume = self.length*self.width*self.height
        print('length', self.length, 'width', self.width, 'height', self.height, 'volume', self._volume)
a1 = Box()
a2 = Box()
a3 = Box()
a4 = Box()
a5 = Box()


for a1 in range(1, 6):
    print('实例化：', a1)
    a1 = Box()
    a1.info()
