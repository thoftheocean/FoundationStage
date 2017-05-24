#!/use/bin/python3

#1python 访问字符串的值
var1='hello'
var2="world"
print("var1[0]:",var1[0])
print("var2[1:5]",var2[1:5])

#2python字符串更新
print("已更新的字符串：",var1+'world')
print("已更新的字符串,helloword的缩写：",var1[0]+'w')

#3python转义字符
print("h\\h") #\\输出\字符
print("\'hello\'") #\'输出 单引号
print("\'hello\'") #\"输出 单引号
print("\a") #\a响铃
print("hello\bworld") #\b退格
print("he\e") #\e转义?
print("\000") #\000空
print("hello\nworld") #\n换行
print("hello\vworld") #\v纵向制表符
print("hello\tworld") #\t横向制表符
print("hello\rworld") #\r回车
print("hello\f") #\f换页
print("hello\other") #\other 其他字符以普通格式输出

#4python字符串运算
a ="Hello"
b ="Python"
print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a *2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if("H"in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")
if("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")
    print(r'\n')
    print(R'\n')
print(r'\n')
print(R'\n')

#5python字符串格式化
print("我是%s是今年%d"%('小明',10))

#6python其他字符
print("%+10x" % 10)
print("%04d" % 5)
pirnt("%6.3f" % 2.3)