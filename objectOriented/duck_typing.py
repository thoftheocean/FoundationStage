# !/usr/bin/env python
# encoding:utf-8
# author:hexi

class Duck:
    def walk(self):
        print('鸭子会走路')

    def run(self):
        print('鸭子也会跑')

class Bird:
    def walk(self):
        print('鸟也会走路')

class Dog:
    def walk(self):
        print('狗也会走路')
    def run(self):
        print('狗也会跑')

def walking(duck):
    duck.walk()
def runing(duck):
    duck.run()

if __name__ == '__main__':
    small_duck = Duck()
    small_Bird = Bird()
    small_dog = Dog()

    walking(small_Bird)
    walking(small_dog)
    walking(small_duck)
    runing(small_duck)
    runing(small_dog)


