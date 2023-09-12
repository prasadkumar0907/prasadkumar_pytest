from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import re


# driver = webdriver.Chrome("./chromedriver")
# driver.get("https://www.ajio.com/")
# driver.find_element_by_xpath("//input[@placeholder='Search AJIO']").send_keys("Shoes")
# driver.find_element_by_xpath("//span[@class='ic-search']").click()
# shoes_ = driver.find_elements_by_xpath("//div[@class='contentHolder']")
# shoe_names = shoes_[:6]
# for shoe in shoe_names:
#     print(shoe.text)
# original_price = [int("".join(re.findall(r"\d",item.text))) for item in driver.find_elements_by_xpath("//span[@class='orginal-price']")[:6]]
# index = original_price.index(max(original_price))
# shoe_names[index].click()
#
# print("the highest original price shoe is")
# print("________")
# print(shoe_names[index].text)


driver = webdriver.Chrome("./chromedriver")

driver.get("https://www.ajio.com/")
driver.maximize_window()
driver.find_element_by_css_selector("input[placeholder='Search AJIO']").send_keys("shoes")
driver.find_element_by_css_selector("span[class='ic-search']").click()
# shoes_ = driver.find_elements_by_xpath("//div[@class='contentHolder']")
# shoe_names = shoes_[:6]
# print(len(shoe_names))
# for shoe in shoe_names:
#     print(shoe.text)
#
# sleep(2)
# driver.close()

# print(shoes_.text)

# driver.maximize_window()
ele_names = driver.find_elements_by_xpath("//div[@class='nameCls']")
ele_prices = driver.find_elements_by_xpath("//span[@class='price  ']")

shoe_names = [ele.text for ele in ele_names]
shoe_prices = [ele.text for ele in ele_prices]

import re
prices = []
for price in shoe_prices:
    match = re.findall(r'\d', price)
    prices.append(int("".join(match)))

pairs = []
for shoe, price in zip(shoe_names, prices):
    pairs.append({'name': shoe, 'price': price})

max_pair = sorted(pairs, key=lambda item: item['price'])[-1]
print(max_pair)
min_price = sorted(pairs, key=lambda item: item['price'])[0]
print(min_price)
price_500_1000 = [item for item in pairs if item['price'] > 500 and item['price'] < 1000]
print(price_500_1000)

