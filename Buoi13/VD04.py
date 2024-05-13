# Đọc dữ liệu từ file csv
import pandas as pd

df = pd.read_csv("marketing-data.csv")

print(df)
print(df.info())
print(df.describe())

print('Số chiều:', df.shape)

print("\n", "7 dòng đầu")
print(df.head(7))

print("\n", "3 dòng cuối")
print(df.tail(3))