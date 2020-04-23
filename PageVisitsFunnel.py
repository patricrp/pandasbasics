import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

#Merge left visits and cart
visits_cart = pd.merge(visits, cart, how='left')
print(visits_cart)

#Length
print(len(visits_cart))

#Null values for cart

print(len(visits_cart[(visits_cart['cart_time'].isnull())]))

#Users who didn't place a t-shirt in their cart

not_cart = float(len(visits_cart[(visits_cart['cart_time'].isnull())])) / float(len(visits_cart))

#Merge left cart and checkout

cart_checkout = pd.merge(cart, checkout, how='left')
print(cart_checkout)

#Users who didn't proceed to checkout

not_checkout = float(len(cart_checkout[(cart_checkout['checkout_time'].isnull())])) / float(len(cart_checkout))

#Merge all

all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')

print(all_data.head())

#Users who did checkout but didn't purchase

checkout_purchase = pd.merge(checkout, purchase, how='left')
not_purchase = float(len(checkout_purchase[(checkout_purchase['purchase_time'].isnull())])) / float(len(checkout_purchase))

#Weakest step of the funnel
print(not_cart)
print(not_checkout)
print(not_purchase)

#Average time to purchase
all_data['time_to_purchase'] = all_data['purchase_time'] - all_data['visit_time']

print(all_data.head())
print(all_data['time_to_purchase'].mean())