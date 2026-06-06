from Product import search_product

def test_product_success():
    assert search_product("laptop")==1000

def test_product_failure():
    assert search_product("Gaming PC")== 2500

def test_product_empty():
    assert search_product(" ")== 2500

def test_product_case():
    assert search_product("Laptop")== 1000  