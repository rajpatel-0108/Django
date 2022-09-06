from wsgiref import headers
import requests
import  json

URL = "http://127.0.0.1:8000/stuapi/"


def get_data(id = None):
    data = {}
    # print(data)
    if id is not None:
        data = {'id':id}
        # print(data)
    json_data = json.dumps(data)
    headers = { 'content-Type': 'application/json' }    
    # print(json_data)
    r = requests.get(url = URL,headers=headers, data=json_data)
    # print(r)
    data = r.json()
    print(data)

get_data()

def post_data():
    data={
        'name':'Jinkal',
        'roll':200,
        'city':'vapi'
    }
    json_data = json.dumps(data)
    headers = { 'content-Type': 'application/json' }
    r = requests.post(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)

# post_data()

def update_data():
    data={
        'id': 8,
        'name':'Rutvi',
        'city':'Kim'
    }
    json_data = json.dumps(data)
    headers = { 'content-Type': 'application/json' }
    r = requests.put(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

# update_data()

def delete_data():
    data={ 'id': 8 }
    json_data = json.dumps(data)
    headers = { 'content-Type': 'application/json' }
    r = requests.delete(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

# delete_data()