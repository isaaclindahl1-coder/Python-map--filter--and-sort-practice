products = [
    {"name": "Keyboard", "price": 45},
    {"name": "Monitor", "price": 180},
    {"name": "Mouse", "price": 25},
    {"name": "Headphones", "price": 75},
    {"name": "USB Drive", "price": 15},
    {"name": "Webcam", "price": 60}
]

passing_price = list(filter(lambda products: products["price"] < 50, products))

print(passing_price)