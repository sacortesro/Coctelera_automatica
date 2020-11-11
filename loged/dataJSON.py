import urllib3,json

http = urllib3.PoolManager()
def jsonSearch(name):
    url="https://www.thecocktaildb.com/api/json/v1/1/search.php?s="+name
    json_url = http.request('GET', url)
    #print(json_url.status)
    data=json.loads(json_url.data)
    return data

#data = json.loads(json_url.read())
#print(data["drinks"].)
#for x in data["drinks"]:
#    print(x.get("strDrink"))    