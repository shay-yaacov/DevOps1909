import requests

response = requests.get('http://localhost:5000/names')

result = response.json()
expected ="Alice"

actual =result[0]["name"]
assert actual == expected   
print (response.text)
print (response.status_code)

