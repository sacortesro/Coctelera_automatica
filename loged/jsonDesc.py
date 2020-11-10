import urllib3,json
#from loged.coctel import idCoctail
http = urllib3.PoolManager()

def fjsonDesc(id):
    url="https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i="+id
    json_url = http.request('GET', url)
    info=json.loads(json_url.data)
    return info

# datos=fjsonDesc("11007")
# print(datos)