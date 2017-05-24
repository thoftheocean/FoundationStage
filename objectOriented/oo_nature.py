# !/usr/bin/env python
# coding:utf-8
# author:hx

class TestClass:
    # 1类属性
    cssa = 'class-attribe'

    def __init__(self):
        # 2实例属性
        self.a = 0
        self.b = 10

    def info(self):
        print('a:', self.a, 'b:', self.b, TestClass.cssa)

    def define_a(self):
        self.c = 19

if __name__ == '__main__':
    # 实例属性

    # tc = TestClass()   # 实例化1
    # tca = TestClass()  # 实例化2
    # tc.info()
    # tca.info()
    # tc.a = 100   #类外修改实例属性
    # tc.b = 200
    # tc.info()
    # tca.info()

    # 类外定义实例属性
    tc = TestClass()
    tc.define_a()
    print(tc.c)

    # 类型修改类属性
    tc = TestClass()
    tc.info()
    TestClass.cssa = 'class-attribe11'
    tc.info()

#3 __的自由属性
class A:
    def __init__(self):
        self.__ab = 0 # 定义的自由属性
    def info(self):
        print(self.__ab)
a = A()
a.info()
a.__ab = 3
a.info() # 自由属性在类的外部是无法修改的
print(a.__ab)

#3 _的自由属性
class A:
    def __init__(self):
        self._ab = 0 # 定义的自由属性
    def info(self):
        print(self.__ab)
a = A()
a.info()
a._ab = 3
a.info() # 自由属性在类的外部是可以修改的
print(a.__ab)

#4 类的特殊属性，不需要定义，本身就包含得有