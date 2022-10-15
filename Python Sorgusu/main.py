import requests

URL = "https://x-math.herokuapp.com/api/random"

param = {
    "max" : "100",
    "min" : "5"
}

result = requests.get(URL, params=param)

data = result.json()

print("\n",data,"\n")
