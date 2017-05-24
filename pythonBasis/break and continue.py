#coding: utf-8
#author: hexi

#实例1
#break
mystr="asdfghjkl"
for i in mystr:
    if i=='h':
        break
    print(i)
print("执行成功")
#continue
'''
mystr="asdfghjkl"
for i in mystr:
    if i=='h':
        continue
    print(i)
print("执行成功")
'''

#实例2
list1=[1,3,5,7]
list2=[2,4,6,8]
new_list=list()
for i in list1:
    for j in list2:
        if j==6:
            break
            #exit() #退出整个程序
        new_list.append([i,j])
    else:
        break
print(new_list)
