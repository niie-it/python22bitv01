'''Write a function to find the length of a string (don't use the len() function)
'''
# Coding Conversion: Python - snake_case
def dem_so_ki_tu(chuoi: str):
    # print(type(chuoi))
    count = 0
    for ki_tu in str(chuoi):
        count += 1
    print(f"{chuoi} có {count} kí tự")
    
# Gọi hàm
dem_so_ki_tu(123456)
dem_so_ki_tu("Anh yêu Python")