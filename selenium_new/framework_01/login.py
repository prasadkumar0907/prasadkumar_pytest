from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.remote.
driver = webdriver.Chrome("./chromedriver")

driver.get("http://demowebshop.tricentis.com")


class _visibility_of_element_located(visibility_of_element_located):

    def __call__(self, driver):
        displayed = super().__call__(driver)
        if isinstance(displayed, WebElement):
            return displayed.is_enabled()
        else:
            return False


wait = WebDriverWait(driver, 20)
v = _visibility_of_element_located(locator)
wait.until(v)


# def click_element(locator):


# def edit_element(locator, *, value):


# sleep(2)





