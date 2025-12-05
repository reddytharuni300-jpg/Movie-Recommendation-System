import requests
import json 
Base_URL = "http://localhost:3000/genres"

def get_genre():
    response = requests.get(Base_URL)
    return response.json()

def add_genre(genre_data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(Base_URL, data=json.dumps(genre_data), headers=headers)
    return response.json()


def update_genre(genre_id, genre_data):
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f"{Base_URL}/{genre_id}", data=json.dumps(genre_data), headers=headers)
    return response.json()

def delete_genre(genre_id):
    response = requests.delete(f"{Base_URL}/{genre_id}")
    return response.json()