'''
Nhập vào số nguyên N
In bảng cửu chương của N
'''

N = int(input("Nhập vào số nguyên: "))
for i in range(1, 11):
    print(f"{N} x {i:2} = {N*i}")
    
# Vui : format
import math
for i in range(111, 222, 10):
    print(f"{i * math.pi:5.3}" )