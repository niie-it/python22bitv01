# Demo_Point.py
from Point import *

diem_a = Point()
diem_a.x = 11
diem_a.y = 5
print(diem_a)
diem_a.output()

diem_b = Point()
diem_b.x = 19
diem_b.y = 5
diem_b.output()

print('Khoảng cách từ A đến B là:', diem_b.calculate_distance(diem_a))