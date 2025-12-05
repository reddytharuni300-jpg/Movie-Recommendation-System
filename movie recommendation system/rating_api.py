from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    return "Hello, Welcome to FastAPI Demo!"

@app.get("/ratings/{movie_title}/") 
def rating_info(movie_title: str):
    return f"Ratings for Movie: {movie_title}"

# Sample rating data  
ratings = [
    {
        "movie_id": 101,
        "rating": 8.8
    },
    {
        "movie_id": 102,
        "rating": 8.7
    },
    {
        "movie_id": 103,
        "rating": 8.4
    }
]

@app.post("/ratings/")
def add_rating(rating: dict):
    ratings.append(rating)
    return {"ratings": ratings}

@app.get("/ratings/")
def get_all_ratings():
    return {"ratings": ratings}

@app.put("/ratings/{movie_id}")
def update_rating(movie_id: int, rating: dict):
    for idx, r in enumerate(ratings):
        if r["movie_id"] == movie_id:
            ratings[idx] = rating
            return {"ratings": ratings}
    return {"error": "Rating not found"}

@app.delete("/ratings/{movie_id}")
def delete_rating(movie_id: int):
    for idx, r in enumerate(ratings):
        if r["movie_id"] == movie_id:
            del ratings[idx]
            return {"ratings": ratings}
    return {"error": "Rating not found"}

@app.get("/ratings/movie/{movie_id}")
def get_ratings_by_movie(movie_id: int):
    movie_ratings = [r for r in ratings if r["movie_id"] == movie_id]
    return {"ratings": movie_ratings}

@app.get("/ratings/user/{user_id}")
def get_ratings_by_user(user_id: int):  
    # Placeholder implementation as user_id is not part of sample data
    return {"ratings": []}

@app.get("/ratings/movie/{movie_id}/average")   
def get_average_rating_for_movie(movie_id: int):
    movie_ratings = [r["rating"] for r in ratings if r["movie_id"] == movie_id]
    if movie_ratings:
        average_rating = sum(movie_ratings) / len(movie_ratings)
        return {"average_rating": average_rating}
    return {"average_rating": None}

@app.get("/ratings/user/{user_id}/average")
def get_average_rating_for_user(user_id: int):
    # Placeholder implementation as user_id is not part of sample data
    return {"average_rating": None} 

    