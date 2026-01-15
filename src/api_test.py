# для проверки API
# обязательно передавать в json
import requests
import json

body = {
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5
}

r = requests.put('http://127.0.0.1:8000/items/1', data=json.dumps(body))
print(str(r.status_code) + " " +  r.text)
