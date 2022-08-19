import requests

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vMTAuMTAuMS42NTo4MDkwL2FwaS9sb2dpbiIsImlhdCI6MTY2MDYzMjUwNywiZXhwIjoxNjYxNDk2NTA3LCJuYmYiOjE2NjA2MzI1MDcsImp0aSI6Imo2UjIzY05SYlI2Y2pjTHkiLCJzdWIiOiI4NzQiLCJwcnYiOiI2ZmFjMWQ5ZjU5OTVhMzkxODNmNmRiYTdkY2QyNDZiNGI5ZGRmMjFkIiwiaWQiOjg3NCwiZmlyc3RfbmFtZSI6ImV6YXoua2giLCJyb2xlIjpudWxsfQ.LcZB4LXhHusHTPLkPoZjLUYJDuET6ToS_vFXa4VKxT8'

response = requests.get('http://10.10.1.74:80/api/v1/catalog/categories/list',headers={
    'Authorization':'Bearer ' + token
})


jsonPython = response.json()

def getFiltered(array,key,value):
    return [item for item in array if item['attributes'][key]==value]

def getFilteredById(array,value):
    return [item for item in array if item['id']==value][0]


filteredSamsungs = getFiltered(jsonPython,'name','Awax')

print(len(filteredSamsungs))


ids = set()

def add_parent_ids(filteredSamsung):
        ids.add(filteredSamsung['id'])
        parentSamsung = getFilteredById(jsonPython,filteredSamsung['attributes'].get('parent_id',None))
        if parentSamsung['attributes']['parent_id'] == None:
            ids.add(parentSamsung['id'])
            return 1
        else:
            ids.add(parentSamsung['id'])
            return add_parent_ids(parentSamsung)
        
    


for filteredSamsung in filteredSamsungs:
    add_parent_ids(filteredSamsung)


print(ids)
print(len(ids))
