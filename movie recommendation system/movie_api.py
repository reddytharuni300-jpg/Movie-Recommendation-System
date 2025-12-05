from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    return "Hello, Welcome to FastAPI Demo!"

@app.get("/movies/{title}/")
def movie_info(title: str):
    return f"Movie Title: {title}"

#Sample movie data
movies = [
        {
      "movie_id": 101,
      "title": "Inception",
      "language": "English",
      "genre_id": 6
    },
    {
      "movie_id": 102,
      "title": "Baahubali",
      "language": "Telugu",
      "genre_id": 1
    },
    {
      "movie_id": 103,
      "title": "3 Idiots",
      "language": "Hindi",
      "genre_id": 2
    }
  ]
@app.post("/movies/")
def add_movie(movie: dict):
    movies.append(movie)
    return {"movies": movies}   

@app.get("/movies/")
def get_all_movies():
    return {"movies": movies}   

@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, movie: dict):
    for idx, m in enumerate(movies):
        if m["id"] == movie_id:
            movies[idx] = movie
            return {"movies": movies}
    return {"error": "Movie not found"}

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    for idx, m in enumerate(movies):
        if m["id"] == movie_id:
            del movies[idx]
            return {"movies": movies}
    return {"error": "Movie not found"}
