import requests

url = "https://api.myanimelist.net/v2/anime?q=one&limit=5"
headers = {
    "X-MAL-CLIENT-ID": "YOUR_CLIENT_ID"
}

res = requests.get(url, headers=headers)
data = res.json()

print(data)

#2nd edit