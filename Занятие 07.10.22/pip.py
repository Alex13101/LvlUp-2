import requests
r = requests.get('https://httpbin.org/anything' )
print(r.text)