'''
BT đổi tiền:
- Nhập số tiền, bội số của 50k
- In số tiền cần đổi biết máy ATM vô hạn và có các mệnh giá:
50k, 100k, 200k, 500k
đơn vị ngàn đồng
'''
print(50 / 3)   # Lấy cả phần thập phân
print(50 % 3)   # Lấy phần dư
print(50 // 3)  # Lấy nguyên

so_tien_doi = int(input("Nhap tien can doi: "))
so_to_500 = so_tien_doi // 500
so_to_200 = (so_tien_doi - so_to_500 * 500) // 200
