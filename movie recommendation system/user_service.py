import requests
import json
Base_URL = "http://localhost:3000/users"


def get_user_preference():
    response = requests.get(Base_URL)
    return response.json()

def add_user_preference(user_data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(Base_URL, data=json.dumps(user_data), headers=headers)
    return response.json()

def update_user_preference(user_id, user_data):
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f"{Base_URL}/{user_id}", data=json.dumps(user_data), headers=headers)
    return response.json()    

def delete_user_preference(user_id):
    response = requests.delete(f"{Base_URL}/{user_id}")
    return response.json()    
    