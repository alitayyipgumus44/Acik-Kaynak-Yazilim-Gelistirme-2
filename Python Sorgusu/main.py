import requests

URL = "https://x-math.herokuapp.com/api/random?max=750&min=150"

result = requests.get(URL)

data = result.json()

print(data)