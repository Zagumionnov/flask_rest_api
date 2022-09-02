import requests

res = requests.post("http://127.0.0.1:5001/api/main/1", json={"name": "C#", "videos": 8})

print(res.json())
