# def even(num):
#     for n in num:
#         if n % 2 == 0:
#             print(f"{n} is an even number")
#         # else:
#         #     print(f"{n} is an odd number")
#
#
# def span(func):
#     def wrapper(*args, **kwargs):
#         try:
#             print(func(*args, **kwargs))
#             file = open("error_msg", 'w')
#             file.write("")
#             file.close()
#         except


# try:
#     print(even([-1,2,4,5]))
#     file = open("error_log.txt", 'w')
#     file.write("")
#     file.close()
# except:
#     file = open("error_log.txt", 'w')
#     file.write("function executed abnormally")
#     file.close()
# finally:
#     with open("error_log.txt", 'r') as file:
#         data = file.read()
#         if data == 'function executed abnormally':
#             print('program did not execute normally')
#         elif data == '':
#             print('executed')
#         else:
#             raise Exception("program terminated abruptly")


# a = 10
# def spam():
#     a = 15
#     print(a)
#     def inner():
#         nonlocal a
#         a += 2
#         print(a)
#     inner()
#
# spam()
# print(a)
#
# a = 10
# def spam():
#     a = 15
#     print(a)
#     def inner():
#         nonlocal a
#         a += 1
#         print(a)
#     inner()
#
# spam()
# print(a)

# try:
#     n = 8
#     d = 0
#     res = n/d
#     print(res)
#     l = [1, 2, 3]
#     print(l[4])
# except (ZeroDivisionError, IndexError):
#     print("division by zero is not allowed")
#     print("index cannot be greater than size of list")
#
# from abc import ABC, abstractmethod
#
#
# class Depreciation(ABC):
#     @abstractmethod
#     def cal_depreciation(self):
#         pass
#
#
# class Vehicle(Depreciation):
#     def __init__(self, actual_cost):
#         self.actual_cost = actual_cost
#
#     def cal_depreciation(self):
#         depreciation_amount = (self.actual_cost * 33)/100
#         return depreciation_amount
#
# car = Vehicle(30000)
# print(car.cal_depreciation())

# from abc import ABC,abstractmethod
#
#
# class Depreciation(ABC):
#     @abstractmethod
#     def cal_depr(self):
#         pass
#
#
# class Vehicle(Depreciation):
#     def __init__(self, actual_cost):
#         self.actual_cost = actual_cost
#
#     def cal_depr(self):
#         depreciated_amt = self.actual_cost * 0.33
#         return depreciated_amt
#
#
# car = Vehicle(30000)
# print(car.cal_depr())


# class Depreciation:
#     depreciated_value = 0
#
#     def __init__(self, depr_method, residual_value):
#         self.depr_method = depr_method
#         self.residual_value = residual_value
#
#     def cal_depreciation(self):
#         if self.depr_method == "SLN":
#             depreciated_value = self.residual_value * 0.33
#             return depreciated_value
#         elif self.depr_method == "SYN":
#             depreciated_value = self.residual_value * 0.15
#             return depreciated_value
#         else:
#             return f"depreciation not applied for this method"
#
#
# d = Depreciation("SLN", 40000)
# print(d.cal_depreciation())
# print(d.depreciated_value)


# class Asset:
#     def info(self, name):
#         print(f"The asset is {name}")
#
#
# class Asset_details(Asset):
#     def __init__(self, cost, useful_years):
#         self.cost = cost
#         self.useful_years = useful_years
#
#     def display(self):
#         super().info("maruti")
#         print(f"the cost of the asset is {self.cost}")
#         print(f"the useful no of years of the asset is {self.useful_years}")
#
#
# car = Asset_details(30000, 4)
# car.display()


# class Asset:
#     def display(name=None, cost=None):
#         print(name, cost)
#
#
# class Child(Asset):
#     def display(name="Base asset", cost=3000):
#         print(name, cost)
#
# car = Child
# car.display()
# car.display("Maruti")
# car.display("Maruti",20000)
#
# l = [1,2,3,4]
# res = (item*2 for item in l)
# print(res)
# print(next(res))

import tracemalloc

def trace_memory(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        res = func(*args, **kwargs)
        print(f"memory usage: {tracemalloc.get_traced_memory()}")
        tracemalloc.stop()
        return res
    return wrapper


@trace_memory
def read_list(num):
    print(num)


@trace_memory
def read_tuple(num):
    print(num)


l = read_list([1,2,3,4])
t = read_tuple((1,2,3,4))





