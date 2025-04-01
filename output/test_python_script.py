import requests

url = 'https://example.com/items'
json_body = {'name': 'item_name'}
response = requests.post(url, json=json_body)
print(response.text)