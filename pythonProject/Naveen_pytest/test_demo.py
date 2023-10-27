import pytest

def test_m1():
    a = 10
    b = 12
    assert a == b+2, "Assertion failes"
    assert a == b, "assertion failed as a is not eq to b"
@pytest.mark.smoke
def test_m2():
    assert True

def test_m3():
    assert False
@pytest.mark.smoke
def test_m4():
    str = "january"
    assert str.upper() == "JANUARY", "assert failed"
    assert str.lower() == "JANUARY", "assert failed as lower is not eq to upper"

def test_m5():
    l = [10, 20, 30]
    assert len(l) == 3

def test_m6():
    print("I am loving python to the core and will crack this interview at any cost")

@pytest.mark.regression
def test_login_chrome():
    assert "login" == "login"