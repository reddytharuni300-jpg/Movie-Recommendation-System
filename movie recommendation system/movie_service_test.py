import movie_service as movie_service

print(" All movies:", movie_service.get_movie_recommendations())
new_movie ={
      "movie_id": 104,
      "title": "Salaar",
      "language": "English",
      "genre_id": 8
    },
added_movie = movie_service.add_movie_recommendation(new_movie) 
print(" Added movie:", added_movie)
updated_movie = {
      "movie_id": 104,
      "title": "Salaar",
      "language": "Telugu",
      "genre_id": 8
    },
movie_id = added_movie.get("id")
print(" Updated movie:", movie_service.update_movie_recommendation(movie_id, updated_movie))    

print(" All movies after addition and update:", movie_service.get_movie_recommendations())

print(" Deleted movie:", movie_service.delete_movie_recommendation(movie_id))

print(" All movies after deletion:", movie_service.get_movie_recommendations())

print(" Movies by genre (Sci-Fi):", movie_service.get_movies_by_genre("Sci-Fi"))

print(" Movies by language (English):", movie_service.get_movies_by_language("English"))

print(" Movies by genre (Sci-Fi) and language (English):", movie_service.get_movies_by_genre_and_language("Sci-Fi", "English"))