from fastapi import FastAPI
import user_service as user_service
import movie_service as movie_service

app = FastAPI()


@app.get("/")
def welcome():
    return {"message": "User service is up and running!"}

@app.get("/users")
def get_all_users():
    return user_service.get_user_preference()  

@app.get("/users/{user_id}") 
def get_user(user_id: int):
    users = user_service.get_user_preference(user_id)
    for user in users:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}

@app.post("/users")
def add_user(user_data: dict):
    return user_service.add_user_preference(user_data)

@app.put("/users/{user_id}")
def update_user(user_id: int, user_data: dict):
    return user_service.update_user_preference(user_id, user_data)

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return user_service.delete_user_preference(user_id)
