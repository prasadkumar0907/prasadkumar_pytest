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
    if item.isnumeric() and int(item) % 2 == 0:
        even_sum += int(item)
print(even_sum)

# another method:
even_sum1 = 0
for char in sentence:
    if '0' <= char <= '9' and int(char) % 2 == 0:
        even_sum1 += int(char)
print(even_sum)

""" create a set of languages starting with "p" """

languages = ["python", "java", "Perl", "PHP", "Python"]

s = set()
s1 = set()
for language in languages:
    if language.startswith('P') or language.startswith('p'):
        s.add(language)
print(s)

for language in languages:
    if language[0] in 'Pp': # if language[0].lower() in 'p'
        s1.add(language)
print(s1)

""" list with only even length string """

languages = ["python", "java", "Perl", "PHP", "Python"]
language1 = []

new_list = [language for language in languages if len(language) % 2 == 0]
print(new_list)

for language in languages:
    if len(language) % 2 == 0:
        language1.append(language)
print(language1)

""" reverse if odd length else keep it as it is """

languages1 = ["python", "java", "Perl", "PHP", "Python", "c++", "node JS"]
new_list1 = []

for language in languages1:
    if len(language) % 2 == 0:
        new_list1.append(language)
    else:
        new_list1.append(language[::-1])
print(new_list1)

# using comprehension:

new_ls = [language if len(language) % 2 == 0 else language[::-1] for language in languages1]
print(new_ls)

""" sum of entire list and sum of internal list"""

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

entire_sum = 0
for lst in l:
    internal_sum = 0
    for item in lst:
        internal_sum += item
    print(f'internal_sum of list {lst} is {internal_sum}')
    entire_sum += internal_sum
print(f'entire_sum of the list is {entire_sum}')

""" list of prime numbers"""

pr_lst = []

for num in range(1, 101):
    if num > 1:
        for n in range(2, num):
            if num % n == 0:
                break
        else:
            pr_lst.append(num)
print(pr_lst)

""" reverse the list """
new_rev=[]
rev_l = ["hi", "hello", "python"]
new_rev.append(rev_l[::-1])
print(new_rev)

""" reverse the list along with the string also reversed"""
rev_l = ["hi", "hello", "python"]
new_rev_lst = []

for item in rev_l[::-1]:
    new_rev_lst.append(item[::-1])
print(new_rev_lst)

""" rotating the list based on k value """

languages = ["python", "java", "Perl", "PHP", "Python"]
k = 3
new_lang = []

for item in range(k-1, len(languages)):
    new_lang.append(languages[item])
for i in range(0, k-1):
    new_lang.append(languages[i])
print(new_lang)

languages = ["python", "java", "Perl", "PHP", "Python"]
k = 3

for i in range(k):
    item = languages.pop()
    languages.insert(0, item)
print(languages)




