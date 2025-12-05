import user_service as user_service

print(" All users:", user_service.get_user_preference())

new_user = {
    "name": "Alice",    
    "preferences": {
        "genre": "Sci-Fi",
        "language": "English"
    }
}
added_user = user_service.add_user_preference(new_user) 
print(" Added user:", added_user)
updated_user = {
    "name": "Alice Smith",    
    "preferences": {
        "genre": "Sci-Fi",
        "language": "English"
    }
}
user_id = added_user.get("id")
print(" Updated user:", user_service.update_user_preference(user_id, updated_user))
print(" All users after addition and update:", user_service.get_user_preferences())
print(" Deleted user:", user_service.delete_user_preference(user_id))
print(" All users after deletion:", user_service.get_user_preferences())