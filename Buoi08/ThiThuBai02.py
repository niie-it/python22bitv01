L = [
    "doublemint,1.5,10",
    "mentos,0.7,20",
    "oreo,2.8,5",
    "chupachups,0.2,30"
]
'''a) Viết chương trình tạo ra một từ điển trong đó các khóa (key, dạng chuỗi) của từ điển là Tên loại kẹo của các
chuỗi trong list đã cho; các giá trị (value, dạng số nguyên) là số lượng hộp kẹo tương ứng với tên loại kẹo.
# Ví dụ: ouput từ điển D là {'doublemint': 10, 'mentos': 20, 'oreo': 5, 'chupachups': 30}'''

D = {}
for item in L:
    arr = item.split(",")
    # print(arr)
    D[arr[0]] = int(arr[2])
print(D)

'''b) In ra khóa trong từ điển tìm được ở câu (a) ứng với giá trị (value) nhỏ nhất. # Ví dụ: khóa với giá trị nhỏ nhât là oreo'''
print(D.items())
# LL = sorted(D.items(), key=lambda kv: (kv[1], kv[0]))
LL = sorted(D.items(), key=lambda kv: kv[1])
print(LL)

'''c) Viết chương trình tính tổng tất cả các giá trị (value) trong từ điển của câu (a). # Ví dụ: tổng là 65'''
S = 0
for item in D:
    S += D[item]
print('S =', S)