#coding:utf-8
#autor:hexi

#实例1买彩票
'''
#开奖号码
nom='23456'
#接收的彩票信息
mynom=input("请输入彩票号码：")
if mynom==nom:
    print('买房，买车去')
else:
    print('继续买彩票')

'''
#实例2判断系统时间是上旬还是下旬，是星期几
import time
# 1获取系统时间
now_time=time.localtime()
# 2得到系统时间的月天数，还有星期几的天数
mday=now_time.tm_mday #当月第几天
wday=now_time.tm_wday #本周周几，0是星期一 6是星期天
result="现在是%s年%s月，并且是当月的" % (now_time.tm_year,now_time.tm_mon)


# 3判断
#判断上旬还是下旬
if mday<=15:
    result +='上旬的'
else:
    result +='下旬的'
#判断今天星期几
if wday==0:
    result +='星期一'
elif wday==1:
    result +='星期二'
elif wday==2:
    result +='星期三'
elif wday==3:
    result +='星期四'
elif wday==4:
    result +='星期五'
elif wday==5:
    result +='星期六'
elif wday==6:
    result +='星期天'
else:
    result +='不会吧，怎么可能！'
print(result)




