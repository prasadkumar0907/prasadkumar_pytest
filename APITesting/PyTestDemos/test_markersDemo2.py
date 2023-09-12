import pytest
import sys


@pytest.mark.skip
def test_login():
    print("login done")


@pytest.mark.skipif(sys.version_info < (3, 11), reason="python version not supported")
def test_addProduct():
    print("add product")



def test_logout():
    print("logout done")