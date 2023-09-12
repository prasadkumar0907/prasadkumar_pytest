from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from framework_01.selenium_wrapper import SeleniumWrapper
from framework_01.config import Config
from pytest import mark

headers = "gender, fname, lname, email, password"

data = [('male', 'steve', 'jobs', 'steve.jobs@company.com', 'password123'),
        ('female', 'laura', 'turner', 'laura.turner@company.com', 'password')]


@mark.parametrize(headers, data)
def test_register(setup, gender, fname, lname, email, password):

    s = SeleniumWrapper(setup)
    if gender == 'male':
        s.click_element((By.ID, "gender-male"))
    else:
        s.click_element((By.ID, 'gender-female'))

    sleep(2)
    s.enter_text((By.ID, "FirstName"), value="hello")

    s.enter_text((By.ID, "LastName"), value="world")

    s.enter_text((By.ID, "Email"), value="helloworld@company.com")

    s.enter_text((By.CSS_SELECTOR, "input[name='Password']"), value="password123")

    s.enter_text((By.CSS_SELECTOR, "input[name='ConfirmPassword']"), value="password123")

    s.click_element((By.XPATH, "//input[@value='Register']"))

    sleep(2)









