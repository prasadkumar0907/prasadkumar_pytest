""" set comprehension to create a set of squares from 1 to 10"""

square_set = set()
# normal method
for num in range(1, 10):
    square_set.add(num ** 2)
print(square_set)

# comprehensions
res = {(num ** 2) for num in range(1, 10)}
print(res)

""" set of tuples with index and item """
list_ = ["Java", "Python", 10, True, 1.4, "c++", "ruby"]

tup = {(index, item) for index, item in enumerate(list_)}
print(tup)

""" set of tuples with item and its length pair """
files = ("Amazon", "flipkart", "walmart", "gmail", "yahoo")

tup1 = {(item, len(item)) for item in files}
print(tup1)


