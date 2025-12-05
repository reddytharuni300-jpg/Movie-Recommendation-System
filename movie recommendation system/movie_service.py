import requests
import json
Base_URL = "http://localhost:3000/movies"

def get_movie_recommendations():
    response = requests.get(Base_URL)
    return response.json()

def add_movie_recommendation(movie_data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(Base_URL, data=json.dumps(movie_data), headers=headers)
    return response.json()
def update_movie_recommendation(movie_id, movie_data):
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f"{Base_URL}/{movie_id}", data=json.dumps(movie_data), headers=headers)
    return response.json()

def delete_movie_recommendation(movie_id):
    response = requests.delete(f"{Base_URL}/{movie_id}")
    return response.json()

def get_movies_by_genre(genre):
    response = requests.get(f"{Base_URL}/genre/{genre}")
    return response.json()
def get_movies_by_language(language):
    response = requests.get(f"{Base_URL}/language/{language}")
    return response.json()

def get_movies_by_genre_and_language(genre, language):  
    response = requests.get(f"{Base_URL}/genre/{genre}/language/{language}")
    return response.json()

def get_movies_by_user_preferences(preferences):
    genre = preferences.get("genre")
    language = preferences.get("language")
    response = requests.get(f"{Base_URL}/genre/{genre}/language/{language}")
    return response.json()            