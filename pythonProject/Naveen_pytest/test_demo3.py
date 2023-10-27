import pytest

def test_m10():
    print(" I love python")

def test_m11():
    print("prearing for ecolabs interview")

def test_m12():
    print("above are the test cases that I am writing to practice pytest for interview")

@pytest.mark.smoke
def test_login_safari():
    assert "login" == "anti-login"