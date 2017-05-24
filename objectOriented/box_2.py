# !/usr/bin/env python
# encoding:utf-8
# author:hx

'''
修改box的作业中定义的类：
1.使用属性包装器将私有属性_color包装为color（可读写）属性
2.运用描述符在Box类中创建一个类属性（盒子六面的图案字符，
只能为数字1－6）
3.为其定义__call__()，当作为函数调用时，返回其体积
'''
class NonNeg:
    def __init__(self, default=0):
        self.default = default

    def __get__(self, instance, owner):
        return self.default

    def __set__(self, instance, value):
        pass


    def __delete__(self, instance):
        pass


class Box:
    box_design = NonNeg()

    def __init__(self):
        self.length = 10
        self.width = 5
        self.height = 8
        self._volume = 0
        self._color = 'red'
        self.buffer = None

    @property
    def color(self):
        return self._color

    def set_lwh(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def set_color(self, color):
        self._color = color
        # print('box color:', self._color)
        return self._color

    def open_Box(self):
        if self.buffer == None:
            print('open box')
        elif self.buffer == 0:
            print('open box')
        else:
            print('不能重复打开')
        self.buffer = 1

    def close_Box(self):
        if self.buffer == None:
            print('close box')
        elif self.buffer == 1:
            print('close box')
        else:
            print('不能重复关闭')
        self.buffer = 0

    def __call__(self):
        self._volume = self.length * self.width * self.height
        return self._volume

    # def info(self):
    #     self._volume = self.length*self.width*self.height
    #     print('box length:', self.length, 'box width:', self.width, 'box height:', self.height, 'box volume:', self._volume)

if __name__ == '__main__':

    a1 = Box()
    a1.set_lwh(1, 3, 5)
    a1.set_color('blue')
    a1.close_Box()
    print(a1.color)
    print(a1())
    a1.width * 2
