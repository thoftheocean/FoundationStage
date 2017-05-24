#coding: utf-8
#author:hx

'''
ZeroDivisionError	除(或取模)零 (所有数据类型)
AttributeError	对象没有这个属性
#open('str.txt','r')
FileNotFoundError找不到文件
ImportError	导入模块/对象失败
IndexError	序列中没有此索引(index)
KeyError映射中没有这个键（ 元组）
NameError	未声明/初始化对象 (没有属性)
SyntaxError	Python 语法错误
IndentationError	缩进错误
TypeError	对类型无效的操作
ValueError
传入无效的参数
'''

'''
捕获异常的语法结构：

try:
<语句>        #运行别的代码
except <异常名>：
<语句>        #如果在try部份引发了'name'异常
except <异常名>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生
finally: #始终会被执行到的代码
<语句>

以上为完整结构，使用的时候至少要有一个try和except代码块。

'''
#
# try:
#     int=2
# except ValueError as e:
#     print('处理了异常:',e)
# else:
#     print('无异常')
# raise TypeError
class  myException(Exception) :
     pass
[['a',1],['a',2],['b',1],['b',2],...]
list1=['a','b','c']
list2=[1,2,3,5]
new_list=[]
try:
    for m in list1:
        for n in list2:
            if n==3:
               raise myException
            new_list.append([m,n])
except myException:
   pass
print(new_list)



