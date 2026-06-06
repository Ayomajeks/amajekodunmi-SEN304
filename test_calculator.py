from calculator import add, divide, multiply
from order import calculate_total

def test_add():
    assert add(2,3) == 5

def test_add_negative():
    assert add(-1,-1) == -2

def test_divide():
    assert divide(10,2) == 5

def test_divide_by_zero():
    try:
        divide(10,0)
        assert False
    except ValueError:
        assert True     

def test_multiply():
    assert multiply(3,4) == 12  

def test_multiply_negative():
    assert multiply(-2, 5) == -10

def test_multiply_total():
    assert multiply_total(100,2) == 200   

