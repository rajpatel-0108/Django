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
    # print(json_data)
    r = requests.get(url = URL, data=json_data)
    # print(r)
    data = r.json()
    print(data)

get_data(1)

def post_data():
    data={
        'name':'Jinkal',
        'roll':200,
        'city':'vapi'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
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
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)

# update_data()

def delete_data():
    data={ 'id': 8 }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)

# delete_data()