# !/usr/bin/env python
# coding:utf-8
# author:hx

'''
修改上次的box
访问私有属性(体积)的方法
添加颜色属性（_color）和设置与获取Box的颜色的方法
添加打开和关闭盒子（Box）的方法，并且限制Box打开（关闭）之后，
再次调用打开（关闭）方法会给予提示；即不能重复打开与关闭。
在主程序中实例化并进行测试。
'''

class Box:
    def __init__(self):
        self.length = 10
        self.width = 5
        self.height = 8
        self._volume = 0
        self._color = 'red'
        self.state = None

    def set_lwh(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def set_color(self, color):
        self._color = color

    def get_color(self):
        print('box color:', self._color)

    def open_box(self):
        if self.state == None:
            print('open box')
        elif self.state == 0:
            print('open box')
        else:
            print('不能重复打开')
        self.state = 1

    def close_box(self):
        if self.state == None:
            print('close box')
        elif self.state == 1:
            print('close box')
        else:
            print('不能重复关闭')
        self.state = 0

    def info(self):
        self._volume = self.length*self.width*self.height
        print('box length:', self.length, 'box width:', self.width, 'box height:', self.height, 'box volume:', self._volume)

if __name__ == '__main__':
    a1 = Box()
    a1.set_lwh(1, 3, 5)
    a1.set_color('blue')
    a1.get_color()
    a1.close_box()
    a1.open_box()
    a1.close_box()
    a1.open_box()
    a1.open_box()
    a1.open_box()
    a1.close_box()
    a1.info()
