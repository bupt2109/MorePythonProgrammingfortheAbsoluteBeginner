# P36-39 print,input,try等python基础知识
import sys
from datetime import datetime, timezone

print("--------------------Print----------------------")
# def print(self, *args, sep=' ', end='\n', file=None) 第2个分隔符，3换行符，4重定向
print("String","Theory",sep='-',end=';')
#打印python版权
print(sys.copyright)
# 打印python版本
print(sys.version)
# 打印操作系统 win32
print(sys.platform)
# 打印时间
print(datetime.now())

print("--------------------Input----------------------")

a = input("Enter a name:")
print(a)

print("--------------------Try----------------------")

s = input("Enter a number:")
try:
    number = float(s)
except:
    number = 0
answer = number * number
print(number, "*", number, "=", answer)

