'''A positive integer with n digits is called an Armstrong number when the sum of the nth powers of its digits is equal to itself.
For example:
371 is Armstrong's number because: 3^3 + 7^3 + 1^3 = 371
8208 is Armstrong's number because: 8^4 + 2^4 + 8^4 = 8208
Check to see if a positive integer entered from the keyboard is an Armstrong number or not?
'''
def is_armstrong(number):
    chuoi_so = str(number)
    n = len(chuoi_so)
    tong = sum(int(so)**n for so in chuoi_so)
    
    return tong == number    

# Demo
n = 371
print(n, ' là số Armstrong?', is_armstrong(n))
m = 8208
print(m, ' là số Armstrong?', is_armstrong(m))
k = 123
print(k, ' là số Armstrong?', is_armstrong(k))