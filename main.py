import requests

print('hello word')

r = requests.get('https://google.com')
print(r.status_code)
