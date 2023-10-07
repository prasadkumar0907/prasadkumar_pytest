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


