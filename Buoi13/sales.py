# import pandas as pd 
# sales=pd.read_csv("sales.csv") # reading from csv file
# print(sales)

# # We will use groupby to count total sale against each product.
# print(sales.groupby(['product','p_id'])[['qty']].sum())


import pandas as pd 
sales=pd.read_csv("sales.csv") 
#print(sales)

# using groupby get the list of products and its sum sold
my_sale=sales.groupby(['product','p_id', 'store'])[['qty']].sum()
#print(my_sale)

product=pd.read_csv("products.csv")
#print(product)
my_sum=pd.merge(my_sale, product, how='left', on='p_id')
#print(my_sum)

#We added one more column total_sales by multiplying total sales with price. 
my_sum['total_sale']=my_sum['qty']*my_sum['price']
print(my_sum)

my_sale=sales.groupby(['product','p_id', 'store'])[['qty']].sum().reset_index()
print(my_sale)


import pandas as pd 
sales=pd.read_csv("sales.csv") 
print(sales.groupby(['product','p_id','store'])[['qty']].sum())


import pandas as pd 
sales=pd.read_csv("sales.csv") 
#print(sales)
product=pd.read_csv("products.csv")
my_sum=pd.merge(sales,product,how='left',on=['p_id'])
my_sum['sales_total']=my_sum['qty']*my_sum['price']
print(my_sum.groupby(['store'])[['qty','sales_total']].sum())


import pandas as pd 
products=pd.read_csv("products.csv") 
sales=pd.read_csv("sales.csv") 
my_data=pd.merge(sales,products,on='p_id',how='right')
#print(my_data['sale_id'].isna())
my_data=my_data[my_data['sale_id'].isnull()] # products which are not sold
print(my_data)
#print(my_data.loc[:,'product_y']) # to display only produts column


import pandas as pd 
sales=pd.read_csv("sales.csv") 
customer=pd.read_csv("customer.csv") 
my_data=pd.merge(sales,customer,on='c_id',how='right')
my_data=my_data[my_data['sale_id'].isnull()] # products which are not sold
#print(my_data)
print(my_data.loc[:,'Customer']) # to display customers who has not purchased 