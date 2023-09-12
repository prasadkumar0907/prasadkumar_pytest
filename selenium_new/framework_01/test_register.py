from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from framework_01.selenium_wrapper import SeleniumWrapper
from framework_01.config import Config

driver = webdriver.Chrome("./chromedriver")
driver.maximize_window()
driver.get(Config.URL)
sleep(3)


#register

s = SeleniumWrapper(driver)

s.click_element((By.ID, "gender-male"))

s.enter_text((By.ID, "FirstName"), value="hello")

s.enter_text((By.ID, "LastName"), value="world")

s.enter_text((By.ID, "Email"), value="helloworld@company.com")

s.enter_text((By.CSS_SELECTOR, "input[name='Password']"), value="password123")

s.enter_text((By.CSS_SELECTOR, "input[name='ConfirmPassword']"), value="password123")

s.click_element((By.XPATH, "//input[@value='Register']"))

sleep(2)


s. click_element((By.CSS_SELECTOR, "a[class='ico-login']"))

s.click_element((By.CSS_SELECTOR, "input[value='Log in']"))

s.enter_text((By.CSS_SELECTOR, "input[id='Email']"), value="helloworld@company.com")

s.enter_text((By.CSS_SELECTOR, "input[id='Password']"), value="password123")

s.click_element((By.CSS_SELECTOR, "input[value='Log in']"))

sleep(2)

driver.close()









