from selenium import webdriver
from time import sleep


driver = webdriver.Chrome("./chromedriver")
# driver.get("http://demowebshop.tricentis.com")
driver.get(r"C:\Users\Admin\Desktop\demo-html\demo.html")

driver.get("http://demowebshop.tricentis.com")
driver.find_element_by_css_selector("a[class='ico-register']").click()
driver.find_element_by_css_selector("input[name='FirstName']").send_keys("hello")
driver.find_element_by_css_selector("input[name='LastName']").send_keys("world")
sleep(2)
# driver.maximize_window()
# current_title = driver.title
# print(current_title)
# sleep(1)
# driver.refresh()
# driver.minimize_window()
# sleep(2)
# driver.maximize_window()
# sleep(2)
# URL = driver.current_url
# print(URL)
# sleep(2)
driver.close()



