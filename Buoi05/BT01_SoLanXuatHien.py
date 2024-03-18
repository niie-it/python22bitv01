'''Đọc file/Nhập chuỗi từ bàn phím.
Thống kê số lần xuất hiện của các từ.'''
import re
chuoi = input("Nhập chuỗi: ").strip()

# Xử lý dấu: dùng .replace() của string hoặc re.sub() của Regex
chuoi = re.sub("[?!:,\"]", "", chuoi)
print('Chuỗi sau xử lý:', chuoi)


# Tách chuỗi thành mảng
mang_tu = chuoi.split() # tách dựa trên khoảng trắng
print(mang_tu)

mang_thong_ke = {} # = { 'anh': 3, 'yêu': 4}
for tu in mang_tu:
    # if tu in mang_thong_ke: # kiểm tra tu có nằm trong các keys
    #     mang_thong_ke[tu] += 1
    # else:
    #     mang_thong_ke[tu] = 1
    mang_thong_ke[tu] = mang_thong_ke.get(tu, 0) + 1
print(mang_thong_ke)