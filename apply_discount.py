prices = [25.00, 50.00, 75.00, 100.00, 150.00]

def discount(price):
    return (price * .8)

discounted_price = list(map(discount, prices))
# print(list(discounted_price))
print(f"Original Price: {prices}")
print(f"Sale Price: {discounted_price}")