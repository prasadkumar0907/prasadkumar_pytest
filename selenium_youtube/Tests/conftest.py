from selenium import webdriver
from Config.config import TestData
from time import sleep
from pytest import fixture


@fixture
def setup():
    driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH)
    driver.maximize_window()
    driver.get(TestData.BASE_URL)
    sleep(3)
    yield driver
    driver.quit()
