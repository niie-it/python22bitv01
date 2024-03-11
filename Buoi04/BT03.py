'''BT3: Write a function to count the number of vowels (a e i o u) and consonants in the string
'''
chuoi = input("Nhập chuỗi: ").strip().lower()
vowels = "ueoai"
consonants="qazwsxedcrfvtgbyhnujmiklop"
vowels_count = 0
consonants_count = 0

for ki_tu in chuoi:
    if ki_tu in vowels:
        vowels_count += 1
    elif ki_tu.isalpha():
        consonants_count += 1
print('consonants:', consonants_count, 'vowels', vowels_count)