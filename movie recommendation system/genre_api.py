from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    return "Hello, Welcome to FastAPI Demo!"

@app.get("/genres/{name}/")
def genre_info(name: str):
    return f"Genre Name: {name}"

#Sample genre data
genres = [  
        {
      "genre_id": 1,
      "name": "Action"
    },
    {
      "genre_id": 2,
      "name": "Comedy"
    },
    {
      "genre_id": 3,
      "name": "Drama"
    }
  ]

@app.post("/genres/")
def add_genre(genre: dict): 
    genres.append(genre)
    return {"genres": genres}

@app.get("/genres/")
def get_all_genres():
    return {"genres": genres}

@app.put("/genres/{genre_id}")
def update_genre(genre_id: int, genre: dict):
    for idx, g in enumerate(genres):
        if g["genre_id"] == genre_id:
            genres[idx] = genre
            return {"genres": genres}
    return {"error": "Genre not found"}

@app.delete("/genres/{genre_id}")
def delete_genre(genre_id: int):    
    for idx, g in enumerate(genres):
        if g["genre_id"] == genre_id:
            del genres[idx]
            return {"genres": genres}
    return {"error": "Genre not found"}

