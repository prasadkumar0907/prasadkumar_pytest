from selenium import webdriver
from framework_01.config import Config
from time import sleep
from pytest import fixture


@fixture
def setup():
    driver = webdriver.Chrome("./chromedriver")
    driver.maximize_window()
    driver.get(Config.URL)
    sleep(3)
    yield driver
    driver.quit()
