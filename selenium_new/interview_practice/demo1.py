# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome('./chromedriver')
# driver.get(r"C:\Users\Admin\Desktop\demo-html\demo.html")
# driver.implicitly_wait(10)
# """Implicit wait should be written only once i.e., after get(URL) line,
# this will automatically be applied for all the find_element and find_elements in the entire code following
# this implicit wait statement"""
# driver.maximize_window()
#
# languages = ['Ruby', 'Java', 'Perl', 'Python', 'C#', 'JavaScript']
#
# for language in languages:
#     _xpath = f"//td[text()='{language}']/..//input[@type='checkbox']"
#     driver.find_element_by_xpath(_xpath).click()
# sleep(2)
# driver.close()

#to click on release notes of  3.9.4 of www.python.org/downloads/ page

# driver.get("https://www.python.org/downloads/")
# driver.maximize_window()
# driver.execute_script("window.scrollBy(0,500)")
# sleep(4)
# _xpath = f"//a[text()='Python 3.9.11']/../..//a[text()='Release Notes']"
#
# driver.find_element_by_xpath(_xpath).click()
# sleep(2)
#
# driver.close()

#to click on corresponding 'add to cart button' of some books and then click on checkbox of any book on cart page

# driver.get("http://demowebshop.tricentis.com")
# driver.maximize_window()
# driver.find_element_by_xpath("//a[contains(text(),'Books')][1]").click()
# driver.execute_script("window.scrollBy(0,500)")
# sleep(3)
# books = ["Health Book", "Fiction", "Computing and Internet"]
#
# for book in books:
#     _xpath = f"//a[text()='{book}']/../..//input[@value='Add to cart']"
#     print(_xpath)
#     driver.find_element_by_xpath(_xpath).click()
#     sleep(2)
#
# sleep(3)
# #to click on the checkbox corresponding to book computing and internet on cart page
#
# driver.get("http://demowebshop.tricentis.com/cart/")
# # driver.maximize_window()
# sleep(5)
#
# driver.find_element_by_xpath("//a[text()='Health Book']/../..//input[@type='checkbox']").click()
# sleep(5)
# driver.close()

#clcicking on radio button of corresponding rating on demowebshop
#
# driver.get("http://demowebshop.tricentis.com")
# driver.maximize_window()
# driver.execute_script("window.scrollBy(0,500)")
# sleep(1)
# options = ['Excellent', 'Good', 'Poor', 'Very bad']
#
# for option in options:
#
#     _xpath = f"//label[text()='{option}']/..//input[@type='radio']"
#     driver.find_element_by_xpath(_xpath).click()
#
# sleep(1)

# driver.get("http://demowebshop.tricentis.com/books")
# driver.execute_script("window.scrollBy(0,500)")
# driver.maximize_window()
#
# expected_prices = {'Science': 51.00, 'Health Book': 10.00, 'Computing and Internet': 10.00, 'Fiction': 24.00}
#
# for book, expected_price in expected_prices.items():
#     _xpath = f"//a[text()='{book}']/../..//span[@class='price actual-price']"
#     actual_price = driver.find_element_by_xpath(_xpath).text
#
#     if float(actual_price) == expected_price:
#         print("Pass")
#     else:
#         print("FAIL")
#
# driver.close()

# driver.get("http://demowebshop.tricentis.com")
# driver.execute_script("window.scrollBy(0,500)")
# driver.maximize_window()
#
# expected_prices = {"$25 Virtual Gift Card": 25.00,
#                    "14.1-inch Laptop": 1590.00,
#                    "Build your own computer": 1100.00
#                    }
#
# for item, expected_price in expected_prices.items():
#     _xpath = f"//a[text()='{item}']/../..//span[@class='price actual-price']"
#     actual_price = driver.find_element_by_xpath(_xpath).text
#
#     if float(actual_price) == expected_price:
#         print("PASS")
#     else:
#         print("FAIL")
#         print(f"Expected price was {expected_price} but the actual price is {actual_price}")
# driver.close()

# driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/sunglasses")
# driver.maximize_window()
# driver.execute_script("window.scrollBy(0,500)")
#
# sun_glasses = {'ORIGINAL COLLECTION': 149.00, 'Custom Sunglasses': 179.00, 'Sunglasses Aero': 139.00}
# print(sun_glasses.items())
# import re
#
# for glass, price in sun_glasses.items():
#     _xpath = f"//a[@title='{glass}']/../..//span[@class='art-price']"
#     actual_price = driver.find_element_by_xpath(_xpath).text
#     actual_price = re.findall(r'\d+.\d+', actual_price)
#     print(actual_price)
#     if float(actual_price[0]) == price:
#         print("PASS")
#     else:
#         print("FAIL")
# sleep(2)
# driver.close()
#
# driver.get("https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market")
# driver.maximize_window()
# print(f"{'company': >10}{'Price': >10}")
# print('-'*30)
#
# companies = ['TCS', 'HDFC', 'MARUTI']
# while True:
#     sleep(5)
#     for company in companies:
#         value = driver.find_element_by_xpath(f"//a[text()='{company}']/../..//td[5]").text
#         print(f"{'company': >10}{'value': >10}")

# driver.get("https://ajio.com")
# driver.find_element_by_name("searchVal").send_keys("Shoes")
# driver.find_element_by_class_name("ic-search").click()
# sleep(3)
# shoes = driver.find_elements_by_class_name("nameCls")
# _xpath = f"//div[@class='nameCls']/..//span[@class='price  ']"
# prices = driver.find_elements_by_xpath(_xpath)
#
# shoes = [shoe.text for shoe in shoes[:6]]
# prices = [price.text for price in prices[:6]]
# import re
# exact_prices = [int(''.join(re.findall(r'\d', price))) for price in prices]
# print(exact_prices)
# print(shoes)
# sleep(2)
# from collections import defaultdict
# pairs = defaultdict(int)
# for shoe, price in zip(shoes, exact_prices):
#     pairs[shoe] = int(price)
#
# # pairs = {shoe: int(price) for shoe, price in zip(shoes, exact_prices)}
#
# max_price = sorted(pairs.items(), key=lambda item: item[1])[-1]
# min_price = sorted(pairs.items(), key=lambda item: item[1])[0]
# price_500_100 = [(shoe, price) for shoe, price in pairs.items() if (price > 500 and price < 1500)]
# print(price_500_100)

# driver.get("http://demowebshop.tricentis.com")
# sleep(2)
# _xpath = f"//div[@class='block block-category-navigation']//a"
# links = driver.find_elements_by_xpath(_xpath)
# for link in links:
#     print(link.text)
# _links_path = f"//div[@class='footer-menu-wrapper']//a"
# footer_links = driver.find_elements_by_xpath(_links_path)
# for flink in footer_links:
#     print(flink.text)
# sleep(2)
# driver.close()

# driver.get("http://monsterindia.com")
# driver.implicitly_wait(2)
# driver.find_element_by_xpath("//input[@id='SE_home_autocomplete']").send_keys("Python")
# sleep(2)
# driver.find_element_by_xpath("//input[@value='Search']").click()
# sleep(3)
# job_titles = driver.find_elements_by_xpath("//div[@class='job-tittle']/h3/a")
# for title in job_titles:
#     print(title.text)
# sleep(1)
# driver.close()
#
# import re
# driver.get("https://www.myntra.com/boys-tshirts")
# driver.find_element_by_xpath("(//label[@class='common-customCheckbox vertical-filters-label']/..//div[@class='common-checkboxIndicator'])[2]").click()
# sleep(3)
# price_tags = driver.find_elements_by_xpath("//div[@class='product-price']")
# for price in price_tags:
#     print(price.text)
#     data = re.findall(r'\d+', price.text)
#     cost = float(data[0])
#     if cost >= 1354 and cost <=2569:
#         print("PASS")
#     else:
#         print("FAIL")

# driver.close()

# from requests import request
#
# driver.get(r"C:\Users\Admin\Desktop\demo-html\links.html")
# sleep(3)
# elements = driver.find_elements_by_xpath("//a")
# links = [element.get_attribute("href") for element in elements]
#
# for link in links:
#     print("SEnding request to the server")
#     response = request("GET", url=link)
#     sleep(3)
#     try:
#         assert response.status_code == 200
#     except AssertionError:
#         print("link is broken")
# sleep(2)
# driver.close()

# import tracemalloc

# def memory(func):
#     def wrapper(*args, **kwargs):
#         tracemalloc.start()
#         result = func(*args, **kwargs)
#         print(f"memory consumed:{tracemalloc.get_traced_memory()}")
#         tracemalloc.stop()
#         return result
#     return wrapper
#
#
# @memory
# def square(numbers):
#     for number in numbers:
#         if number % 2 == 0:
#             yield number
#
# @memory
# def evens(a):
#     for num in a:
#         res = [num for num in a if num % 2 == 0]
#         return res

#
# l = [1, 2, 3, 4]
# l_ = iter(l[::-1])
#
# class list_:
#     def __init__(self, start, end):
#         self.value = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.value >= self.end:
#             raise StopIteration
#         current = self.value
#         self.value += 1
#         return current
# #
# l = list_(1, 10)
# print(next(l))
# print(next(l))

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver.exe")
# driver.get(r"C:\Users\Admin\Desktop\demo-html\demo.html")
# sleep(3)

# elements = driver.find_elements_by_xpath("//input[@class='alert']")
# for item in elements:
#     item.click()
#     sleep(3)
#
# driver.find_element_by_xpath("//button[text()='Delete']").click()
# sleep(1)
# driver.switch_to.alert.accept()
# sleep(1)
#
# driver.find_element_by_xpath("//button[text()='Delete']").click()
# sleep(1)
# driver.switch_to.alert.dismiss()
# sleep(2)

# driver.get("http://demowebshop.tricentis.com/computing-and-internet")
# sleep(3)
#
# driver.find_element_by_xpath("//a[@title='Facebook']").click()
# sleep(2)
#
# handles = driver.window_handles
# driver.switch_to.window(handles[1])
#
# driver.find_element_by_name("email").send_keys("hello.world@company.com")
# driver.close()
#
# driver.switch_to.window(handles[0])
# sleep(2)

# driver.get("https://crossbrowsertesting.github.io/drag-and-drop.html")
# source_ele = driver.find_element_by_id("draggable")
#
# target_ele = driver.find_element_by_id("droppable")
#
# actions = ActionChains(driver)
#
# actions.drag_and_drop(source_ele, target_ele).perform()

driver.get("https://www.myntra.com")
sleep(3)
actions = ActionChains(driver)

# profile =driver.find_element_by_xpath("//span[text()='Profile']")

# actions.move_to_element(profile).perform()

# driver.find_element_by_xpath("//a[text()='login / Signup']").click()

actions.send_keys(Keys.PAGE_DOWN).perform()

# def func(num):
#     for i in range(len(num)):
#         yield num[i]
#
#
# g = func([1, 2, 3, 4])
# print(next(g))
# print(next(g))

#
# class list_:
#
#     def __init__(self, start, end):
#         self.value = start
#         self.end = end
#
#     def __iter__(self):
#
#         return self

    # def __next__(self):
    #     if self.value >= self.end:
    #         raise StopIteration
    #     current = self.value
    #     self.value += 1
    #     return current
#
# l = list_(1, 10)
#
# for num in l:
#     print(num)
#
# # l2 = list_(1, 5)
# # print(next(l2))
# # print(next(l2))
#
# def spam(num):
#     for i in range(len(num)):
#         yield num[i]
#
# g = spam([1, 2, 3, 4])
# print(next(g))
# print(next(g))

# def my_range(start, end):
#     current = start
#     while current < end:
#         yield current
#         current += 1
#
#
# nums = my_range(1, 10)

# for num in nums:
#     print(num)

# print(next(nums))
# print(next(nums))

# files = ['youtube.txt', 'amazon.txt', 'apple.xls', 'flipkart.in']
#
# for item in files:
#     a = item.split('.')
#     if len(a[0]) % 2 == 0:
#         break
#     else:
#         print(a[0])






