# class Triangle:
#     def __init__(self, a, b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def cal_perimeter(self):
#         perimeter = self.a + self.b + self.c
#         return perimeter
#
#
# t1 = Triangle(2, 3, 5)
# print(t1.cal_perimeter())


"""Inheritance"""
#
# class Polygon:
#     def __init__(self, sides):
#         self.sides = sides
#
#     def display(self):
#         print("Polygon is a 2 dimensional shape with straight lines")
#
#     def get_perimeter(self):
#         perimeter = sum(self.sides)
#         return perimeter
#
#
# class Triangle(Polygon):
#     def display(self):
#         super().display()
#         return f"Triangle is 3 sided shape"
#
#
# class Quadrilateral(Polygon):
#     def display(self):
#         super().display()
#         print("Quadrilateral is a 4 sided shape")
#
#
# t1 = Triangle([3, 4, 5])
# print(t1.get_perimeter())
# print(t1.display())

# q1 = Quadrilateral([1, 2, 3, 4])
# print(q1.get_perimeter())


# def avg_marks(marks, num_of_subjects):
#     total_marks = sum(marks)
#     avg = total_marks/num_of_subjects
#     return avg
#
#
# result = avg_marks([45, 35, 50, 65], 4)
# print(result)

# def fibonacci(i):
#     # start = 0
#     # next = 1
#     # for i in range(0, len(number)):
#     if i == 0:
#         return 0
#     elif i == 1:
#         return 1
#     else:
#         return fibonacci(i-2) + fibonacci(i-1)
#
#
# print(fibonacci(5))
# for i in range(10):
#     print(fibonacci(i))


# print(fibonacci(5))
# num = 5467
# num2 = 0
# while num > 0:
#
#     temp = num % 10
#     num2 = (num2*10) + temp
#     num = num // 10
# print(num2)

# num = 3456
# num2 = 0
# while num > 0:
#     remainder = num % 10
#     num2 = (num2 * 10) + remainder
#     num = num // 10
# print(num2)

# d = {5: True, 7: False, 8: True}
# li = [key for key, value in d.items() if value == True]
# print(li)
#
# d1 = {key:"pass" if value == True else value for key, value in d.items()}
# print(d1)
#
# d.__setitem__(6, False)
# print(d)
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def display(self):
#         print("Hi", self.name)
#         print("You got", self.marks)
#
#     def grade(self):
#         if self.marks >= 60:
#             print("First Grade")
#         elif self.marks >= 50:
#             print("Second grade")
#         elif self.marks >= 35:
#             print("Third grade")
#         else:
#             print("You failed")
#
#
# n = int(input("enter the number of students:"))
# # for i in range(n):
# count = 1
# while count <= n:
#     name = input("Enter the name:")
#     marks = int(input("Enter the marks"))
#     print("*"*20)
#     s = Student(name, marks)
#     s.display()
#     s.grade()
#     count += 1

class Student:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks

    def display(self):
        print("Hi", self.name)
        print("You got", self.marks)
    #
    # def grade(self):
    #     if self.marks >= 60:
    #         print("First Grade")
    #     elif self.marks >= 50:
    #         print("Second grade")
    #     elif self.marks >= 35:
    #         print("Third grade")
    #     else:
    #         print("You failed")

# n = int(input("enter the number of students:"))
# # for i in range(n):
# count = 1
# while count <= n:
#     name = input("Enter the name:")
#     marks = int(input("Enter the marks"))
#     print("*"*20)
#     s = Student()
#     s.setName(name)
#     s.setMarks(marks)
#     s.display()
#     s.grade()
#     count += 1

# s = Student()
# s.setName("jwala")
# print(s.name)
# # s.setMarks = 34
# # # print(s.name)
# print(s.getName())
# # s.display()


# class Asset:
#     def __init__(self, __name, __useful_life, __initial_cost):
#         self.name = __name
#         self.__useful_life = __useful_life
#         self.__initial_cost = __initial_cost
#
#     def display(self):
#         print("Name:", self.name)
#         print("Useful life:", self.__useful_life)
#         print("Initial cost:", self.__initial_cost)
#
#
# car = Asset("Maruthi", 3, 500000)
# car.display()
# print(car._Asset__name)
# print(Asset.__dict__)
# print(car.__dict__)
# print(car._Asset__name)

# from abc import ABC, abstractmethod
#
#
# class Depreciation():
#     __depreciated_value = 0
#
#     def __init__(self, depr_method, residual_value):
#         self.depr_method = depr_method
#         self.residual_value = residual_value
#
#     def cal_depreciation(self):
#         if self.depr_method == "SLN":
#             __depreciated_value = self.residual_value * 0.33
#             print(__depreciated_value)
#         elif self.depr_method == "SYDM":
#             __depreciated_value = self.residual_value * 0.27
#             print(__depreciated_value)
#         else:
#             return f"No depreciation for this method {self.depr_method}"
#
#
# table = Depreciation("SLN", 4500)
# table.cal_depreciation()
# print(table.__depreciated_value)

# class Vehicles(Depreciation):
#     def __init__(self, act_cost):
#         self.act_cost = act_cost
#
#     def cal_depreciation(self):
#         depreciated_amount = self.act_cost * 33/100
#         return depreciated_amount
#
#
# car = Vehicles(230000)
# print(car.cal_depreciation())

# from threading import *
#
# def test1():
#     # print("executing by", current_thread().name)
#     for _ in range(5):
#         # print(f"This is {current_thread().name}", end="\n")
#         print('child thread')
#
# def test2():
#     for _ in range(5):
#         print("child1 thread")
#
# t1=Thread(target=test1)
#
# t2= Thread(target=test2)
#
# t1.start()
# t2.start()
# # print("executing by:", current_thread().name)
# for i in range(5):
#     # print(f"This is {current_thread().name}", end="\n")
#     print('main thread')

# from threading import *
#
# def test1():
#     print("executing child thread1", current_thread().name)
#     for _ in range(5):
#         print("Child1 thread")
#
# def test2():
#     print("executing child thread2", current_thread().name)
#     for _ in range(5):
#         print("Child2 thread")
#
# t1 = Thread(target=test1)
#
# t2 = Thread(target=test2)
#
# t1.start()
# t2.start()
#
# for _ in range(3):
#     print("executing main thread", current_thread().name)
#     print("main thread")
#
# from threading import *
#
# class MyThread(Thread):
#     def run(self):
#         for i in range(5):
#             print("child thread", current_thread().name)
#
#
# t2=MyThread()
# t1 = MyThread()
# t1.start()
# t2.start()

# from selenium import webdriver
#
# driver = webdriver.Chrome("./chromedriver")
# driver.get("https://google.com")
# driver.get_screenshot_as_file(r"C:\Users\Admin\PycharmProjects\selenium_youtube\screenshots\post.png")

# class Asset:
#     Bank_name = "OBC"
#
#     def __init__(self, asset_name):
#         self.asset_name = asset_name
#
#     @classmethod
#     def change_name(cls, bank_name):
#         Asset.Bank_name = bank_name
#
#
# a = Asset("cycle")
# print(a.Bank_name)
# a.change_name("SBI")
# print(a.Bank_name)

class Greet:
    def greeting(self, name=None):
        if name is not None:
            print("Hello",name)
        else:
            print("Hello")


obj=Greet()
obj.greeting("Sai")
obj.greeting()

