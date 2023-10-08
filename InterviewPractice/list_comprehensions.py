""" WAP to create a list of squares for the elements in the below list"""
l = [1, 2, 3, 4, 5]

res = []

for item in l:
    res.append(item ** 2)
print(res)

res = [item ** 2 for item in l]
print(res)

res = [pow(item, 2) for item in l]
print(res)

""" create list of tuples of index and its corresponding item in the list """
l = ["python", 10, 3.2, "selenium", "Java"]
res = []
for index, item in enumerate(l):
    res.append((index, item))
print(res)

res = [(index, item)for index, item in enumerate(l)]
print(res)

""" list of even numbers """

l1 = list(range(10))
l2 = []
for index in l1:
    if l1[index] % 2 == 0:
        l2.append(l1[index])
print(l2)

for item in l1:
    if item % 2 == 0:
        l2.append(item)
print(l2)

l2 = [item for item in l1 if item % 2 == 0]
print(l2)

""" list of even and odd """
l1 = list(range(10))
el = []
ol = []

for item in l1:
    if item % 2 == 0:
        el.append(item)
    else:
        ol.append(item)
print(f'even list ={el} and ol={ol}')

el1 = []
ol1 = []
l_new = [el1.append(item) if item % 2 == 0 else ol1.append(item) for item in l1]
print(f'even list ={el1} and ol={ol1}')

en = [item for item in l1 if item % 2 == 0]
on = [item for item in l1 if item % 2 != 0]
print(f'en={en} and on={on}')

""" if even store as it is else reverse and store it """
ls = ["python", "Node JS", "oracle", "Java", "SQL"]
new_ls = []

for word in ls:
    if len(word) % 2 == 0:
        new_ls.append(word)
    else:
        new_ls.append(word[::-1])
print(new_ls)

# using comprehensions

new_cls = [word if len(word) % 2 == 0 else word[::-1] for word in ls]
print(new_cls)

""" reverse if it is a string else keep it as it is """
list_ = ["Java", "Python", 10, True, 1.4, "c++", "ruby"]

# using comprehension
new_list = [item[::-1] if isinstance(item, str) else item for item in list_]
print(new_list)

# normal method
new_list1=[]
for item in list_:
    if isinstance(item,str):
        new_list1.append(item[::-1])
    else:
        new_list1.append(item)
print(new_list1)

""" list of words starting with vowel """
files = ["Amazon", "flipkart", "walmart", "gmail", "yahoo", "internet explorer"]

# using comprehensions
vowel_string = [word for word in files if word[0].lower() in 'aeiou']
print(vowel_string)

# normal method
vw_str = []
for word in files:
    if word[0].lower() in 'aeiou':
        vw_str.append(word)
print(vw_str)




















