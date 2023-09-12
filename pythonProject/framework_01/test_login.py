from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from framework_01.selenium_wrapper import SeleniumWrapper
from framework_01.config import Config
from pytest import mark

headers = 'email, password'

data = [('bill.gates@company.com', 'password123'), ('hello.world@company.com', 'password123')]


@mark.parametrize(headers, data)
def test_login(setup, email, password):

    s = SeleniumWrapper(setup)

    s. click_element((By.CSS_SELECTOR, "a[class='ico-login']"))

    s.click_element((By.CSS_SELECTOR, "input[value='Log in']"))

    s.enter_text((By.CSS_SELECTOR, "input[id='Email']"), value="helloworld@company.com")

    s.enter_text((By.CSS_SELECTOR, "input[id='Password']"), value="password123")

    s.click_element((By.CSS_SELECTOR, "input[value='Log in']"))

    sleep(2)
