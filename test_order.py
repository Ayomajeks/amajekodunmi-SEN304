from Order import create_order

def test_order_success():
    assert create_order(1000, 5)== 5000

def test_order_zero_value():
    assert create_order(1000, 0)== 0

def test_order_negative():
    assert create_order(1000, -1)== -1000    