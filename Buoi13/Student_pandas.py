# 1. Read the excel file, to create the DataFrame.
import pandas as pd 
my_data = pd.read_excel('student.xlsx',index_col='id')
print(my_data)

# 2. How many rows and columns are there?
print(my_data.shape) # ( 35, 4)


# 3. Read the first 4 rows
print(my_data.head(4))

# 4. How many rows are there?
print(my_data.columns)

# 5. Display the first 5 records of NAME column of the DataFrame
print(my_data['name'][:5]) # Five rows of name column

# 6. Display highest 5 records based on the MARK column.
my_dt=my_data.sort_values(['mark'],ascending=False)
print(my_dt[:5])

# 7. Display all classes in CLASS column ( Unique class )
print(my_data['class'].unique())
