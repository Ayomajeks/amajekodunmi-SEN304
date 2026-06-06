from Payment import make_payment

def test_payment_success():
    assert make_payment(1000)==True

def test_payment_zero_value():
    assert make_payment(0)==False

def test_payment_negative():
    assert make_payment(-1)==False   