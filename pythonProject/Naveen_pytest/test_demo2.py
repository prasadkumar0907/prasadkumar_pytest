import pytest

def test_m7():
    str = "january"
    assert str.upper() == "JANUARy", "assert failed"
    assert str.lower() == "january", "assert failed as lower is not eq to upper"
@pytest.mark.regression
def test_m8():
    l = [10, 20, 30]
    assert len(l) == 3
    assert len(l) == 2

def test_m9():
    print("I am loving python to the core and will crack this interview at any cost")

def test_login_IE():
    assert "login" == "login"