import requests

url = 'http://127.0.0.1:5000/ville'
data = {'ville': 'kolwezi', 'pays': 'rdc'}
x = requests.post(url, json = data)

url = 'http://127.0.0.1:5000/ville'
y = requests.get(url, json = data)

url = 'http://127.0.0.1:5000/ville'
z = requests.put(url, json = data)

url = 'http://127.0.0.1:5000/ville'
a = requests.DELETE(url, json = data)
