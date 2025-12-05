import requests
import json 

Base_URL = "http://localhost:3000/ratings"

def get_movie_ratings():
    response = requests.get(Base_URL)
    return response.json()

def add_movie_rating(rating_data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(Base_URL, data=json.dumps(rating_data), headers=headers)
    return response.json()

def update_movie_rating(rating_id, rating_data):
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f"{Base_URL}/{rating_id}", data=json.dumps(rating_data), headers=headers)
    return response.json()

def delete_movie_rating(rating_id):
    response = requests.delete(f"{Base_URL}/{rating_id}")
    return response.json()

def get_ratings_by_movie(movie_id):
    response = requests.get(f"{Base_URL}/movie/{movie_id}")
    return response.json()

def get_ratings_by_user(user_id):
    response = requests.get(f"{Base_URL}/user/{user_id}")
    return response.json()

def get_average_rating_for_movie(movie_id):
    response = requests.get(f"{Base_URL}/movie/{movie_id}/average")
    return response.json()

def get_average_rating_for_user(user_id):
    response = requests.get(f"{Base_URL}/user/{user_id}/average")
    return response.json()