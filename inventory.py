import codecademylib
import pandas as pd

df = pd.read_csv('inventory.csv')

dfs = df.head(10)

product_request = dfs['product_description'].tolist()

print(product_request)

seed_request = df[(df['product_type'] == 'seeds') & (df['location'] == 'Brooklyn')]

print(seed_request)

mylambda = lambda x: 'True' if x > 0 else False

df['in_stock'] = df['quantity'].apply(mylambda)


df['total_value'] = df['price'] * df['quantity']

combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)

df['full_description'] = df.apply(combine_lambda, axis=1)