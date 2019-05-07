import requests
res = requests.get("http://127.0.0.1:5000/api/flights/11")
print(res.json())
print(res.status_code)
