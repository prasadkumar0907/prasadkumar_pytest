from selenium import webdriver
from selenium.webdriver.support.select import Select
from framework_01.wait import _wait


class SeleniumWrapper:

    def __init__(self, driver):
        self.driver = driver

    @_wait
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @_wait
    def enter_text(self, locator, value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    @_wait
    def select_item(self, locator, item):
        ele = self.driver.find_element(locator)
        s = Select(ele)
        if isinstance(item, str):
            s.select_by_visible_text(item)
        elif isinstance(item, int):
            s.select_by_index(item)
        else:
            return TypeError
