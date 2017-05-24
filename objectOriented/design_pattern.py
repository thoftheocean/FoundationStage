# 单例模式
# class SingleClass:
#     def __init__(self, x=0):
#         self.x = 0
#
# sc = SingleClass()
#
# def tsc1():
#     print(sc.x)
#     sc.x = 10
#     print(sc.x)
#
# def tsc2():
#     print(sc.x)
#     sc.x = 9
#     print(sc.x)
#
# if __name__ == '__main__':
#     tsc1()
#     tsc2()

# # 单例模式2
# class SingleClass:
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls,'_sgl'):
#             cls._sgl = super().__new__(cls, *args, **kwargs)
#         return cls._sgl
#
# if __name__ == '__main__':
#     sa = SingleClass()
#     sb = SingleClass()
#     print(id(sa))
#     print(id(sb))

# 工厂模式
# class Ab:
#     a = 3
# class Ac:
#     a = 0
# class MyFactory:
#     def get_instance(self, ins):
#         return ins()
#
# if __name__ == '__main__':
#     my = MyFactory()
#     print(type(my.get_instance(Ab)))
#     print(type(my.get_instance(Ac)))

# # 策略模式-类作为参数进行传递
# class Moveable:
#     def move(self):
#         print('move....')
# class MoveOnFeet(Moveable):
#     def move(self):
#         print('move on feet')
#
# class MoveOnWheel(Moveable):
#     def move(self):
#         print('move on wheel')
# class Test:
#     def move(self):
#         print('i am fly')
#
# class MoveObj:
#     def set_move(self, moveable):
#         self.moveable = moveable()
#
#     def move(self):
#         self.moveable.move()
#
# if __name__ == '__main__':
#     m = MoveObj()
#     m.set_move(Moveable)
#     m.move()
#     m.set_move(MoveOnFeet)
#     m.move()
#     m.set_move(MoveOnWheel)
#     m.move()
#     m.set_move(Test)
#     m.move()

# #策略模式 -函数作为参数进行传递
# def movea():
#     print('move a')
#
# def moveb():
#     print('move b')
#
#
# class MoveObj:
#     def set_move(self, moveable):
#         self.moveable = moveable
#
#     def move(self):
#         self.moveable()
#
# if __name__ == '__main__':
#     m = MoveObj()
#     m.set_move(movea)
#     m.move()
#     m.set_move(moveb)
#     m.move()

# 装饰模式
# class BeDeco:
#     def be_edit_fun(self):
#         print('Sourece fun')
#
#     def be_keep_fun(self):
#         print('keep fun')
#
# class Decorater:
#     def __init__(self, dec):
#         self._dec = dec()
#
#     def be_edit_fun(self):
#         print('start ...')
#         self._dec.be_edit_fun()
#
#     def be_keep_fun(self):
#         self._dec.be_keep_fun()
#
# if __name__ == '__main__':
#     bd = BeDeco()
#     bd.be_edit_fun()
#     bd.be_keep_fun()
#
#     dr = Decorater(BeDeco)
#     dr.be_edit_fun()
#     dr.be_keep_fun()

# 装饰模式2
# class Water:
#     def __init__(self):
#         self.name = 'Water'
#
#     def show(self):
#         print(self.name)
#
# class Deco:
#     def show(self):
#         print(self.name)
#
# class Sugar(Deco):
#     def __init__(self, water):
#         self.name = 'Sugar'
#         self.water = water
#
#     def show(self):
#         print(self.name)
#         print(self.water.name)
# class Salt(Deco):
#     def __init__(self, water):
#         self.name = 'Salt'
#         self.water = water
#
#     def show(self):
#         print(self.name)
#         print(self.water.name)
#
# if __name__ == '__main__':
#     w = Water()
#     s = Sugar(w)
#     s.show()
#
#     s = Salt(w)
#     s.show()

# 类装饰器

# def deco(a_class):
#     class NewClass:
#         def __init__(self, age, color):
#             self.wrapped = a_class(age)
#             self.color = color
#
#         def display(self):
#             print(self.color)
#             print(self.wrapped.age)
#     return NewClass
#
# @deco
# class Cat:
#     def __init__(self, age):
#         self.age = age
#
#     def display(self):
#         print(self.age)
#
# if __name__ == '__main__':
#     c = Cat(12, 'black')
#     c.display()

# 观察者模式
'''
# 模式特点：定义了一种一对多的关系，让多个观察对象同时监听一个主题对象，
# 当主题对象状态发生变化时会通知所有观察者。

# 程序实例：公司里有两种上班时趁老板不在时偷懒的员工：
# 看NBA的和看股票行情的，并且事先让老板秘书当老板出现时通知他们继续做手头上的工作
'''
#抽象的观察者
class Obserber:

    def __init__(self, strname, strsub):
        self.name = strname
        self.sub = strsub

    def Update(self):
        pass


# 具体的观察者
class StockObserver(Obserber):
    def Update(self):
        print(u'%s:%s,停止看股票,继续工作!' % (self.name, self.sub.action))


# 具体观察者
class NBAObserver(Obserber):
    def Update(self):
        print(u'%s:%s,停止看股票,继续工作!' % (self.name, self.sub.action))


# 规则(主题) -->抽象
class SecretarytBase:

    def __init__(self):
        self.observer = []

    def Attach(self, new_observer):
        pass

    def deleteobserver(self, new_observer):
        pass

    def Notify(self):
        pass


class Secretary(SecretarytBase):

    def Attach(self, new_observer):  # 添加
        self.observer.append(new_observer)

    def Notify(self):
        for p in self.observer:  # 2
            p.Update()

if __name__ == '__main__':
    p = Secretary()
    s1 = StockObserver('Tom', p)
    s2 = NBAObserver('Jack', p)
    p.Attach(s1)
    p.Attach(s2)
    p.action = "WARNING:BOSS"
    p.Notify()



