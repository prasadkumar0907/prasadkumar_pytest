import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    print("start browser")
    yield
    print("close browser")


def test_1(setup):
    print("test1 executed")


def test_2(setup):
    print("test2 executed")


def test_3(setup):
    print("test3 executed")



