""" WAP to create a dictionary with item and its index pair"""

# normal method

string = 'hello'
# l = string.split() --------> will get the string itself, hence it doesn't word
d = {}

for index, item in enumerate(string):
    d[index] = item
print(d)
# print(l)

# comprehension

d = {index: item for index, item in enumerate(string)}

'''
""" WAP to create a dictionary with word and its length pair"""
sentence = "hello world welcome to python"
words = sentence.split()
dict_ = {}
for word in words:
    dict_[word] = len(word)
print(dict_)

dict1 = {word: len(word) for word in words}
print(dict1)

""" create a dictionary of character and its count"""
s = "hello world"
sl = list(s)
d = {}
for char in s:
    d[char] = s.count(char)
print(d)

dict_ = {char: s.count(char) for char in s}
print(dict_)

""" create a dictionary of word and its count"""
sentence1 = "python is a language, python programming is easy"
words = sentence1.split()
word_dict = {}

for word in words:
    word_dict[word] = words.count(word)
print(word_dict)

# comprehensions

dict_ = {word: words.count(word) for word in words}
print(dict_)

""" dictionary with word and its count pair only if the word is of even length"""

sentence2 = "python is a lovely language, python programming is easy and I love it to the core"
words = sentence2.split()
dict_ = {}
print(words)

for word in words:
    if len(word) % 2 == 0:
        dict_[word] = words.count(word)
print(dict_)

dict_word = {word: words.count(word) for word in words if len(word) % 2 == 0}
print(dict_word)
'''
""" dictionary with index and word pair if the word is of odd length reverse it,
else keep it as is"""

sentence3 = "python is a lovely language, python programming is easy and I love it to the core"
words = sentence3.split()
dict_3 = {}

for index, word in enumerate(words):
    if len(word) % 2 == 0:
        dict_3[index] = word
    else:
        dict_3[index] = word[::-1]

print(dict_3)

dict_31 = {index: word if len(word) % 2 == 0 else word[::-1] for index, word in enumerate(words)}
print(dict_31)

"""WAP to create a dictionary of word and length pair only if the word is starting with vowel """

sentence = "python is a language, python programming is easy and I am loving it"
words = sentence.split()
vowel_dict = {}
for word in words:
    if word[0].lower() in 'aeiou':
        vowel_dict[word] = len(word)
print(vowel_dict)

vowel_dict1 = {word: len(word) for word in words if word[0].lower() in 'aeiou'}
print(vowel_dict1)

""" index and word pair if word is of type string reverse it """
list_ = ["python", 17, 9, "java", 19.9, 4+0j, "ruby", "c++"]
str_dict = {}

for index, word in enumerate(list_):
    if type(word) == str:
        str_dict[index] = word[::-1]
    else:
        str_dict[index] = word
print(str_dict)

# or

for index, item in enumerate(list_):
    if isinstance(item, str):
        str_dict[index] = item[::-1]
    else:
        str_dict[index] = item
print(str_dict)

str_dict_rev = {index: word[::-1] if type(word) == str else word for index, word in enumerate(list_)}
print(str_dict_rev)

""" index and word pair if word is of type string keep it as it else reverse it """
list_ = ["python", 17, 9, "java", 19.9, 4+0j, "ruby", "c++"]
rev_dict = {}

for index, word in enumerate(list_):
    if isinstance(word, str):
        rev_dict[index] = word
    else:
        rev_dict[index] = str(word)[::-1]
print(rev_dict)

d1 = {index: item if isinstance(item, str) else str(item)[::-1] for index, item in enumerate(list_)}
print(d1)

""" flip keys and values in a dictionary """
dict_ = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

keys_values = {value: key for key, value in dict_.items()}
print(keys_values)

""" char and ascii value pair """
string = "python"

ascii_dict = {char: ord(char) for char in string}
print(ascii_dict)
