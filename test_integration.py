from Login import login
from Product import search_product
from Order import create_order
from Payment import make_payment

def test_full_purchase_flow():
    assert login("admin", "password123") == True

    price = search_product("laptop")
    assert price == 1000

    total = create_order(price, 2)
    assert total == 2000

    payment = make_payment(total)
    assert payment == True