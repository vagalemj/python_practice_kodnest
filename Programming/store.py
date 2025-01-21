dic = {}
while True:
    prod = input().strip()
    if prod == 'done':
        break
    product, price = prod.split(', ')
    product = product.strip()
    price = price.strip()
    dic[product] = price

for product, price in dic.items():
    print(f'{product}, {price}')