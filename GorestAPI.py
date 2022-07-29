from urllib import response
import requests
import json
import jsonpath

url_post = "https://gorest.co.in/public/v2/users"

file = open("C:\\Users\\Dell Latitude\\Desktop\\API Testing\\createUser.json",'r')
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)

response_post = requests.post(url_post,request_json)
print(response_post.content)
status = response_post.status_code
print(status)
print(response_post.headers.get('Date'))
response_post_json = json.loads(response_post.text)


url_get = "https://gorest.co.in/public/v2/users/24"
response_get=requests.get(url_get)
print(response_get)
print(response_get.content)
#print(response_get.headers)
json_response_get =json.loads(response_get.text)
print(json_response_get)

pages = jsonpath.jsonpath(json_response_get,'email')
print(pages[0])
assert pages[0] == 'chidaakaash_menon_pres@bauch-rippin.info'

