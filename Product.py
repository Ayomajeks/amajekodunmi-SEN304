products = {
    "laptop": 1000,
    "phone": 500,
    "tablet": 300
}

def search_product(product_name):
    return products.get(product_name, None)