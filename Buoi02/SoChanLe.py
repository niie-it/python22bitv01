'''
Viết chương trình nhập vào một số nguyên và cho biết số nguyên đó là số chẵn hay số lẻ.
'''
number = int(input("Please input a number: "))
if number % 2 == 0:
    print(f"{number} is even number")
else:
    print(f"{number} is odd number")