danh_sach_khoa = [
    { 'ten': 'CNTT', 'soluong': 700, 'nam': '2012'},
    { 'ten': 'LY', 'soluong': 300, 'nam': '2008'},
    { 'ten': 'HOA', 'soluong': 200, 'nam': '2010'},
    { 'ten': 'TOAN', 'soluong': 500, 'nam': '2000'}
]
'''
a) Viết chương trình tạo ra một list chứa số lượng sinh viên của tất cả các Khoa trong list đã cho và được sắp xếp
theo thứ tự tăng dần.
#Ví dụ: output như sau: [200, 300, 500, 700]'''
so_svs = []
for khoa in danh_sach_khoa:
    so_svs.append(khoa["soluong"])
sorted_sosv = sorted(so_svs)
print(sorted_sosv)

# a') DS các khoa giảm dần theo số lượng sv
ds_khoa_sort = sorted(danh_sach_khoa, key=lambda k : k["soluong"], reverse=True)
print(ds_khoa_sort)
'''b) Viết chương trình tìm tên Khoa có thời gian thành lập lâu nhất tính đến nay. #Ví dụ: output là TOAN'''
for khoa in danh_sach_khoa:
    khoa["nam"] = int(khoa["nam"])

'''c) Viết chương trình tìm các Khoa có số lượng sinh viên lớn hơn 200. In kết quả các Khoa tìm được ra màn hình
theo thứ tự tăng dần theo từ điển.
#Ví dụ: output là CNTT, LY, TOAN'''
ten_khoas = []
for khoa in danh_sach_khoa:
    if khoa["soluong"] > 200:
        ten_khoas.append(khoa["ten"])
print(sorted(ten_khoas))