import requests

url = "https://api.themoviedb.org/3/movie/122"

payload = "{}"
response = requests.request("GET", url, data=payload)

print response.text