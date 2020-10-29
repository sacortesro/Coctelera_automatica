import urllib3,json

http = urllib3.PoolManager()

url="https://www.thecocktaildb.com/api/json/v1/1/list.php?c=list"
json_url = http.request('GET', url)
#print(json_url.status)
data=json.loads(json_url.data)
#data = json.loads(json_url.read())
for x in data["drinks"]:
    print(x.get("strCategory"))    