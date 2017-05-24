#coding: utf-8
#author: hexi
'''
#while循环语句
mystr="shfdjdsla"
i=0
while i<len(mystr):
    print(mystr[i])
    i=i+1
else:
    print('循环顺利并结束')
'''

'''
#for循环语句
mystr="shfdjdsla"
for i in mystr:
    print(i)
for(i,v) in enumerate(mystr):
    print(i,v)
else:
    print("循环出错")
'''

#循环实例
#while循环
num=0
sum=0
while num<=100:
    if num%2!=0:
        sum+=num
    num+=1
print(sum)
#for循环
sum=0
for num in range(1,101):
    if num%2!=0:
        sum+=num
    num+=1
print(sum)





