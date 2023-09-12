import requests
import json

p = {'page': 2}
url = "https://reqres.in/api/users"
response = requests.get(url, params=p)
print(response.url)
json_data = response.json()
print(json_data['total'])
assert json_data['total'] == 12, "not matching"
print(json_data['total_pages'])
assert json_data['total_pages'] == 2, "its not two"
print(json_data['data'][0]['email'])
assert (json_data['data'][0]['email']).endswith("reqres.in"), "email is not matching"
print(json_data['data'][0]['first_name'])
assert (json_data['data'][0]['first_name']) == 'Michael', "first name not matching"
print(json_data['data'][2]['last_name'])
assert json_data['data'][2]['last_name'] != None, "last name not matching"
print(json_data['support']['url'])
assert json_data['support']['url'] == "https://reqres.in/#support-heading", "url is not matching"



















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
