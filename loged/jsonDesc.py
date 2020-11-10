import urllib3,json

http = urllib3.PoolManager()

url="https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=11007"
json_url = http.request('GET', url)
info=json.loads(json_url.data)
