import genre_service as genre_service   

print(" All genres:", genre_service.get_genre())
new_genre = {
    "name": "Sci-Fi"
}
added_genre = genre_service.add_genre(new_genre)
print(" Added genre:", added_genre)

updated_genre = {
    "name": "Science Fiction"   
}
genre_id = added_genre.get("id")
print(" Updated genre:", genre_service.update_genre(genre_id, updated_genre))   
print(" All genres after addition and update:", genre_service.get_all_genres())

print(" Deleted genre:", genre_service.delete_genre(genre_id))
print(" All genres after deletion:", genre_service.get_all_genres())

print(" Genre by ID:", genre_service.get_genre_by_id(genre_id))
print(" Genre by name:", genre_service.get_genre_by_name("Science Fiction"))

print(" Movies by genre (Science Fiction):", genre_service.get_movies_by_genre("Science Fiction"))

print(" Genres with movie counts:", genre_service.get_genres_with_movie_counts())

print(" Genres with average ratings:", genre_service.get_genres_with_average_ratings())        