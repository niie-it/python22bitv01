import pandas as pd

data = {"calories": [420, 380, 390],
        "duration": [50, 40, 45]
    }
#load data into a DataFrame object
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)
print()

#use a list of indexes:
print(df.loc['day1'])
print()
# refer to the row index:
print(df.loc[['day1', 'day3']])
# return one or more specified row(s)
