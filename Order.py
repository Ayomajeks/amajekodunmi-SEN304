def create_order(product_price, quantity):
    if quantity <= 0:
        raise ValueError("Invalid quantity")
    return product_price * quantity    