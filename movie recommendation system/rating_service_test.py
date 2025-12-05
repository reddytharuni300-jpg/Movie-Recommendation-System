import rating_service as rating_service

print(" All ratings:", rating_service.get_movie_ratings())

new_rating = {
    "movie_id": 1,  
    "user_id": 1,    
    "rating": 9.0       
}
added_rating = rating_service.add_movie_rating(new_rating)
print(" Added rating:", added_rating)

updated_rating = {
    "movie_id": 1,
    "user_id": 1,
    "rating": 9.5
}
rating_id = added_rating.get("id")  
print(" Updated rating:", rating_service.update_movie_rating(rating_id, updated_rating))
print(" All ratings after addition and update:", rating_service.get_movie_ratings())

print(" Deleted rating:", rating_service.delete_movie_rating(rating_id))
print(" All ratings after deletion:", rating_service.get_movie_ratings())

print(" Ratings by movie (ID 1):", rating_service.get_ratings_by_movie(1))
print(" Ratings by user (ID 1):", rating_service.get_ratings_by_user(1))

print(" Average rating for movie (ID 1):", rating_service.get_average_rating_for_movie(1))
print(" Average rating for user (ID 1):", rating_service.get_average_rating_for_user(1))