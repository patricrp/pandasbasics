import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

ad_clicks_grouped = ad_clicks.groupby('utm_source')['user_id'].count().reset_index()
print(ad_clicks_grouped.head())

ad_clicks['is_click'] = ~ad_clicks['ad_click_timestamp'].isnull()

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click'])['user_id'].count().reset_index()

print(clicks_by_source)

clicks_pivot = pd.pivot_table(data=clicks_by_source, values='user_id', index='utm_source', columns='is_click').reset_index()

print(clicks_pivot)

clicks_pivot['percent_clicked'] = clicks_pivot[True]/(clicks_pivot[False]+clicks_pivot[True])

experimental = ad_clicks.groupby(['experimental_group', 'is_click'])['user_id'].count().reset_index()
print(experimental)

pivoted = pd.pivot_table(data= experimental, values='user_id', index='experimental_group', columns='is_click').reset_index()

print(pivoted)

a_clicks = ad_clicks[(ad_clicks['experimental_group'] == 'A')]

b_clicks = ad_clicks[(ad_clicks['experimental_group'] == 'B')]

a_group = a_clicks.groupby(['is_click','day'])['user_id'].count().reset_index()
print(a_group)

a_pivot = pd.pivot_table(data=a_group, values='user_id', index='day', columns='is_click').reset_index()


a_pivot['percentage_True'] = a_pivot[True]/(a_pivot[True]+a_pivot[False])
print(a_pivot)

b_group = b_clicks.groupby(['is_click','day'])['user_id'].count().reset_index()
print(b_group)

b_pivot = pd.pivot_table(data=b_group, values='user_id', index='day', columns='is_click').reset_index()

b_pivot['percentage_Tru'] = b_pivot[True]/(b_pivot[True]+b_pivot[False])
print(b_pivot)