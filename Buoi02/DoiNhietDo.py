'''
Viết chương trình nhập một giá trị là độ °C (Celsius) và chuyển nó sang độ °F (Fahrenheit).
Nhập vào giá trị độ °C muốn chuyển đổi
Tính độ °F tương ứng qua công thức: °F  =  ( °C × 1.8 ) +  32
Hiển thị độ °F (In ra màn hình)
'''
try:
    do_c = int(input("Nhập độ °C: "))

    do_f = (do_c * 1.8) + 32

    print("Độ F=", do_f)
except Exception as ex:
    print(ex)