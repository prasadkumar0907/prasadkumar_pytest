'''WAP to count the number of digits and chars in a given string'''

string = '1234stringcount245@'
char_count = 0
digit_count = 0

for char in string:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        char_count += 1
    elif '0' <= char <= '9':
        digit_count += 1

print(f'the character count in the given string is {char_count} and digit count is {digit_count}')

'''Create a string by swapping the case'''

string = 'hELLO World'

res = ''

for char in string:
    if 'a' <= char <= 'z':
        res += chr(ord(char)-32)
    elif 'A' <= char <= 'Z':
        res += chr(ord(char)+32)
    else:
        res += char
print(res)

#another methof using string function swapcase:

res = string.swapcase()
print(res)

# search for a character and return it's first occurrence index

string = 'happy python'
char='p'
i = 0

for item in string:
    if item == char:
        print(f'the {char} is at position {i}')
        break
    i += 1


for item in string:
    if item == char:
        ind = string.index(char)
        print(f'the {char} is at position {ind}')
        break

for index, character in enumerate(string):
     if char == character:
         print(f'the {char} is at position {index}')
         break

for index in range(len(string)):
    if char == string[index]:
        print(f'the {char} is ar position {index}')
        break

""" print char and ascii value if it is a vowel"""
s = "HellO"
# l= ['a','e','i','o','u']

for char in s:
    if char in 'aeiouAEIOU':
        print(f"the vowel character is {char} and it's ascii value is {ord(char)}")

for char in s:
    if char.lower() in 'aeiou':
        print(char, ord(char))

""" print word and its length"""
s = "hello python I love you"
new_s = s.split()
for index, word in enumerate(new_s):
    print(word, len(word))

for word in new_s:
    print(word, len(word))

""" print words starting with vowels """
sentence = " ai everyone, elcome to the python class"
l_sentence = sentence.split()

for word in l_sentence:
    if word[0].lower() in 'aeiou':
        print(word)

""" count the characters without any inbuilt functions """
s = "hello world"
count=0

for char in s:
    count += 1
print(count)

""" reversing a string """
string = "hello"
new_word=''

print(string[::-1])

for char in reversed(string):
    new_word = new_word+char

print(new_word)

for index in range(len(string)-1,-1,-1):
    print(string[index], end="")
print()

# Python Program to Copy a String

string = 'Hello'
string1 = string[:]
print(string1)

string2 = ''
for char in string:
    string2 = string2+char
print(string2)

# Python program to Count Occurrence of a Character in a String

str_o = 'love python'
str1 = list(str_o)
for char in str1:
    print(char, str1.count(char))















