from time import sleep

from selenium import webdriver

def test_chrome():
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get("https://google.com")
    driver.maximize_window()
    sleep(1)
    assert driver.title == "Google"
    driver.quit()

def test_facebook():
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get("https://facebook.com")
    driver.maximize_window()
    sleep(1)
    assert driver.title == "Facebook – log in or sign up"
    driver.quit()

def test_instagram():
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get("https://instagram.com")
    driver.maximize_window()
    driver.implicitly_wait(3)
    assert driver.title == "Instagram"
    driver.quit()

def test_twitter():
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get("https://twitter.com")
    driver.maximize_window()
    sleep(1)
    driver.implicitly_wait(3)
    assert driver.title == 'X. It’s what’s happening / X'
    driver.quit()

def test_gmail():
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get("https://gmail.com")
    driver.maximize_window()
    sleep(1)
    assert driver.title == "Gmail"
    driver.quit()


