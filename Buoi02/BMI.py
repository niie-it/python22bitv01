'''Nhập vào chiều cao (cm) và cân nặng (kg), tính số BMI và xét rồi xin kết quả theo dữ liệu sau:
# BMI = cân nặng / (chiều cao ^ 2)
BMI < 16: Gầy cấp độ III
16 <= BMI < 17: Gầy cấp độ II
17<= BMI < 18.5: Gầy cấp độ I
18.5 <= BMI < 25: Bình thường
25 <= BMI < 30: Thừa cân
30 <= BMI < 35 : Béo phì cấp độ I
35 <= BMI < 40: Béo phì cấp độ II
BMI > 40: Béo phì cấp độ III'''

chieu_cao = int(input("Nhập chiều cao (cm): ")) / 100
can_nang = float(input("Nhập cân nặng (kq): "))

BMI = can_nang / (chieu_cao ** 2)
print(f"Nặng: {can_nang} kg, cao: {chieu_cao} m, BMI={BMI}")

if BMI < 16:
    print("Gầy cấp độ III")
elif BMI < 17:
    print("Gầy cấp độ II")
elif BMI < 18.5:
    print("Gầy cấp độ I")
elif BMI < 25:
    print("Bình thường")
elif BMI < 30:
    print("Thừa cân")
elif BMI < 35:
    print("Béo phì cấp độ I")
elif BMI < 40:
    print("Béo phì cấp độ II")
else:
    print("Béo phì cấp độ III")
