'''
Display Fibonacci series up to n terms
Example: n = 10  1  1  2  3  5  8  13  21  34  55
'''
fibo = [1, 1]
N = int(input("Nhập vào số nguyên: "))
while len(fibo) < N:
    s = len(fibo)
    #  fibo = fibo + [fibo[s-1] + fibo[s-2]]
    fibo.append(fibo[s-1] + fibo[s-2])

print(fibo)   