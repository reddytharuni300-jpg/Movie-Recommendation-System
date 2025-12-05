from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    return "Hello, Welcome to FastAPI Demo!"


@app.get("/{name}/{college}")
def greet(name: str, college: str):
    return f"Hello, {name} from {college}! Welcome to FastAPI Demo!"   

#students = [101, 102, 103, 104]


#@app.post("/students/{student_id}")
#def add_student(student_id: int):
#    students.append(student_id)
#    return {"students": students}

#wanted to check with proper student details
students = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Jane"},
    {"id": 3, "name": "Doe"}
]

@app.get("/students/")
def get_all_students():
    return {"students": students}

@app.post("/students/")
def add_student(student: dict):
    students.append(student)
    return {"students": students}   

    