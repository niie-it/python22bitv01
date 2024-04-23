import sqlite3

conn = sqlite3.connect("MyDB.db")
cur = conn.cursor()
# cur.execute('''CREATE TABLE HocVien
# (
#     MaHV text PRIMARY KEY,
#     HoTen text,
#     DienThoai text,
#     NgaySinh date,
#     Email text
# )
# ''')

# Demo thêm dữ liệu
mahv = 'HV001'
hoten = 'Trần Văn Tèo'
dienthoai = '009009900'
email = 'myinfo@hienlth.io.vn'
ngaysinh = '2004-11-29'
sql = f"""
INSERT INTO HocVien(MaHV, HoTen, NgaySinh, DienThoai, Email)
VALUES('{mahv}', '{hoten}', '{ngaysinh}', '{dienthoai}', '{email}')
"""
# print(sql)
conn.execute(sql)

conn.commit()
conn.close()
