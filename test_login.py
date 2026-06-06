from Login import login

def test_login_success():
    assert login("admin", "password123")==True

def test_login_failure():
    assert login("user", "wrong")==False    