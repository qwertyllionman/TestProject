from typing import List
from fastapi import FastAPI, HTTPException
from models import Student, Test, TestResult, ResponseMessage
from starlette import status
app = FastAPI()

students:List['Student'] = []
tests:List['Test'] = []
results:List['TestResult'] = []
messages:List['ResponseMessage'] = []
database = [students, tests, results, messages]

@app.post("/students/", status_code=status.HTTP_201_CREATED)
async def create_student(student:Student):
    students.append(student)
    return {"message" : "Student created successfully!"}

@app.get("/students/{student_id}/", status_code=status.HTTP_200_OK)
async def get_student(student_id:int):
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student is not found!")

@app.get("/students/", status_code=status.HTTP_200_OK)
async def get_all_students():
    return students
