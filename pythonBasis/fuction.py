#coding: utf-8
#author: hexi


def myfuction(name):
    print('你好')
    print("我是%s" % name)

myfuction("何喜")


'''
def myfuction(name="何喜"):
    print('你好')
    print("我是%s" % name)

myfuction("张三") #会对name重新赋值
myfuction()

'''
'''
def myfuction(name="何喜",age=20,*agr):  #不确定参数个数时用*var
    print('你好')
    print("我是%s" % name)
    print(agr)
myfuction("张三",20,34,56,76)

'''

# def myfuction(name="何喜",age=20,*agr,**agr2):  #不确定参数个数时用*var
#     print('你好')
#     print("我是%s" % name)
#     print(agr)
#     print(agr2)
#     return 'hello' #有返还值，后面的语句是不执行的
#     print('很高兴见到你')
# myfuction("张三",20,34,56,76,sex='男')

# def myfuction()
#
#     list1=[1,3,5,7]
#     list2=[2,4,6,8]
#     new_list=[]
#     new_list=list()
#         for i in list1:
#            for j in list2:
#               if j==6:
#                   return new_list  #遇到6时直接跳出所有循环
#             #exit() #退出整个程序
#         new_list.append([i,j])
#  print(new_list)

# #某一个区间的数字求和
# def myfuction(start,end):
#     sum=0
#     while start<=end:
#         if start%2!=0:
#             sum+=start
#         start+=1
#     return sum
# print(myfuction(10,1000))

#匿名函数（lambda）
# lambda :print('我是何喜')





