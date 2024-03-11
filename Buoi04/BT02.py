'''Write a program to count the number of words in a string (assume the words in the string are separated by a space)
'''
chuoi = input("Nhập chuỗi: ")
# Tách chuỗi thành mảng (defualt phân cách theo khoảng trắng) dùng hàm: chuoi.split()
mang_tu = chuoi.split()
print('Có', len(mang_tu), 'từ')

