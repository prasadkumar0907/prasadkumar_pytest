import requests
import json

url = "https://reqres.in/api/users?page=2"
# response = requests.get(url)
# print(response)
# print(response.content)
# print(response.headers)

# url = "https://reqres.in/api/users/2"
response = requests.get(url)
print(response)
code = response.status_code
assert code == 200, "Unexpected code"
print(response.json())
print(response.headers)
print(response.cookies)
print(response.encoding)
print(response.url)















# print(type(response))
# print(response.text)
# print(response.content)
# print(response.json())


# code = response.status_code
# try:
#     assert code == 201, "code doesn't match"
# except AssertionError:
#     print("code doesn't match")


# print(response.content)
# print(response.json())
# data = json.loads(response.text)
# print(data)
