from selenium import webdriver
import pytest


@pytest.fixture()
def set_up():
    driver = webdriver.Chrome("./chromedriver.exe")
    yield driver
    driver.close()

