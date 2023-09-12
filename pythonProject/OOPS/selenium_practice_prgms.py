from selenium import webdriver

from time import sleep

driver = webdriver.Chrome("./chromedriver.exe")
# driver.get("http://demowebshop.tricentis.com/books")
driver.maximize_window()
sleep(1)

# expected_prices = {'Science': 51.00, 'Health Book': 10.00, 'Computing and Internet': 10.00, 'Fiction': 24.00}
#
# for book, expected_price in expected_prices.items():
#     _xpath = f"//a[text()= '{book}']/../..//span[@class='price actual-price']"
#     actual_price = driver.find_element_by_xpath(_xpath).text
#     print(actual_price)
#
#
#
# # print(item.text)
# driver.close()

driver.get("http://demowebshop.tricentis.com/")

expected_prices = { '$'}

