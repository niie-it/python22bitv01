'''
Randomly generate a Vietlott MEGA645 lottery ticket with 6 numbers, each number belongs to [1, 45]
HINT:
    Using list []
    Add a element to list: .append(element)
    Using random library:
        from random import *
        number = randint(1, 45)
'''
from random import *
bo_so = []
while len(bo_so) < 6:
    so_ngau_nhien = randint(1, 45)
    if so_ngau_nhien not in bo_so:
        bo_so.append(so_ngau_nhien)
        
print("Bộ số của bạn:", bo_so)
bo_so.sort()
print("Bộ số của bạn:", bo_so)