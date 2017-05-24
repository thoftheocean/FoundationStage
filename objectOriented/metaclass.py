# class Custom:
#     def __init__(self):
#         print('init method')
#
#     def __new__(cls, *args, **kwargs):
#         print('new instance')
#         return object.__new__(cls, *args, **kwargs)
#
# if __name__ == '__main__':
#     Custom()

class MyMeta(type):
    def __init__(self, name, bases, dicts):
        print('init instance')

    def __new__(cls, name, bases, dicts):
        dicts['info'] = lambda self: print('Djx')  #创建了info方法（输出Djx）
        res = type.__new__(cls, name, bases, dicts) #创建的新类
        res.company = 'maizi' #创建了一个类属性
        return res

#自定义元类
#python3.x版本下
class custom(metaclass=MyMeta):
    pass

#python2.x版本下
# class cus():
#     metaclass= MyMeta
#     pass

if __name__ == '__main__':
    cus = custom()
    cus.info()
    print(cus.company)