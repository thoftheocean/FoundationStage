'''
1 打开文件
2阅读\写入
3关闭
'''
# #1 打开文件
# f=open('record.text','w',encoding='utf-8') #指定一个编码格式，可以防止中写入文乱码
# #2 写入
# f.write('hello.world')
# #3关闭
# f.close()


# #1 打开文件
# f=open('record.text','r+',encoding='utf-8') #指定一个编码格式，可以防止中写入文乱码
# #2 阅读
# print(f.readline())
# #3关闭
# f.close()

# #阅读代码简化
# with open('record.txt','r+',encoding='utf-8')as f:
#     print(f.readline())

'''
文件操作实战：
接收用户的输入，并将用户输入的内容以追加的方式写入到文件，直到用户输
入exit或者quit则退出程序，退出的时候显示文件中所有记录的内容。

分析
1。一直接受。输入exit或quit退出
2.追加的方式
3退出时显示所有记录的内容
'''
while True:
    mystr=input("请输入信息：")
    #f mystr=='exit' or mystr=='quit':
    if mystr in ['exit','quit']:
        with open('record.text','r',encoding='utf')as f:
            for v in f:
                print(v,end=' ')
        break
    with open('record.text','a+',encoding='utf-8')as f:
        f.write(mystr+'\n')






