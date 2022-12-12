from requests import put, get
print(get('http://127.0.0.1:5000/bar?key1=val1&key2=12.34').json())