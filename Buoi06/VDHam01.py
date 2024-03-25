'''Demo định nghĩa hàm'''

def say_hello(name = 'Tèo'):
    print(f"Hello {name}.")
    return

def calculate(x, y):
    return x**y / (x - y)

def _no_access_():
    print("Do not print")

if __name__ == "__main__":
    # Gọi hàm
    say_hello('Anh')
    result = calculate(11, 7)
    print("Kết quả tính:", result)
    print(calculate(y=11, x=7))