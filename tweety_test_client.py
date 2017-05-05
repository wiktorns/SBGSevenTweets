import requests

req = requests.post('http://127.0.0.1:5000/tweets?tweet=first')
print('{} {}'.format(req.status_code, req.text))

req = requests.post('http://127.0.0.1:5000/tweets?tweet=second')
print('{} {}'.format(req.status_code, req.text))

req = requests.post('http://127.0.0.1:5000/tweets?tweet=third')
print('{} {}'.format(req.status_code, req.text))

req = requests.get('http://127.0.0.1:5000/tweets/2')
print('{} {}'.format(req.status_code, req.text))

req = requests.get('http://127.0.0.1:5000/tweets')
print('{} {}'.format(req.status_code, req.text))

req = requests.delete('http://127.0.0.1:5000/tweets/3')
print('{} {}'.format(req.status_code, req.text))

req = requests.delete('http://127.0.0.1:5000/tweets/5')
print('{} {}'.format(req.status_code, req.text))

req = requests.get('http://127.0.0.1:5000/tweets')
print('{} {}'.format(req.status_code, req.text))