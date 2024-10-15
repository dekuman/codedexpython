
stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x):
    return stock_prices[x-1]

def max_price(a,b):
    req_stock= stock_prices[a-1:b]
    return max(req_stock)

def min_price(a,b):
    req_stock= stock_prices[a-1:b]
    return min(req_stock)

print(price_at(1))
print(max_price(1,10))
print(min_price(1,10))


