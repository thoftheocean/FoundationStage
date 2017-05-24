# !/usr/bin/env python
# encoding:utf-8
# author:hx

'''
1.具有6个面，每个面为一种颜色
2.每种颜色代表一个数值（1－6）
3.实现一个通过颜色计算两种其代表数值和的静态方法
4.实现一个类方法（gen_dice）用于产生这个类的实例
'''

class Box:
    def __init__(self):
        self.red = 1
        self.black = 2
        self.white = 3
        self.yellow = 4
        self.pink = 5
        self.purple = 6

    @staticmethod
    def cal_val(color1, color2):
        return color1 + color2

    # @classmethod
    # def gen_dice(cls):
    #     a3 = Box()
    #     return a3

    def gen_dice(self):
        a3 = Box()
        return a3

if __name__ == '__main__':
    a = Box()
    b = a.gen_dice()

    # a = Box.gen_dice()
    # b = Box()
    print(a.cal_val(a.red, a.black)) # 调用的是类型实例
    print(b.cal_val(a.red, b.black))  # 调用的是类型实例