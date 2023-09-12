# def prime(number):
#
#     for i in range(2, number):
#
#         if number % i == 0:
#             return f"The number is not prime"
#
#         return f"The given number is a prime number"
# #
# #
# print(prime(6))

# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome("./chromedriver.exe")
# driver.get("http://demowebshop.tricentis.com")
# driver.execute_script("window.scrollBy,(0,500)")
# sleep(2)
# driver.close()

# Python program showing
# a scope of object

def some_func():
    print("Inside some_func")

    def some_inner_func():
        var = 10
        print("Inside inner function, value of var:", var)

    some_inner_func()
    print("Try printing var from outer function: ", var)


some_func()


