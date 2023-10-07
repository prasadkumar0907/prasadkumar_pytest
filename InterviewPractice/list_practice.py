#WAP to remove all duplicates
"""
names=['apple','google','apple','yahoo', 'google']
new_names=set(names)
print(new_names)
"""

#WAP to print all numeric values in a list

"""
items = ['apple', 12.6, 'google', 1.2, 26, 100]
for item in items:
    if isinstance(item, (int, float, complex)):
        print(item)
"""

"""WAP to sum all even numbers in the given string"""

sentence = "hello 123 world 567 welcome to 9724 python"
even_sum = 0
sentence_list = list(sentence)
print(sentence_list)
for item in sentence_list:
    if isinstance(item, int):
        if item % 2 == 0:
            even_sum = even_sum+item
            
print(even_sum)