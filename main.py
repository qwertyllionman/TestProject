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

@app.post("/tests/", status_code=status.HTTP_201_CREATED)
async def create_test(test:Test):
    tests.append(test)
    return {"message" : "Test created successfully!"}

@app.get("/tests/{test_id}/", status_code=status.HTTP_200_OK)
async def get_test(test_id:int):
    for test in tests:
        if test.id == test_id:
            return test
    raise HTTPException(status_code=404, detail="Test is not found!")

@app.get("/tests/", status_code=status.HTTP_200_OK)
async def get_all_tests():
    return tests

@app.post('/results/', status_code=status.HTTP_201_CREATED)
async def submit_test(submission:TestResult):
    results.append(submission)
    return {"message":"Test result is submitted successfully"}

@app.get('/results/student/{student_id}/', status_code=status.HTTP_200_OK)
async def get_test_for_student(student_id:int):
    res = []
    for result in results:
        if result.student_id == student_id:
            res.append(result)
    if res:
        return res
    raise HTTPException(status_code=404, detail="Student results not found!")

@app.get('/results/test/{test_id}/', status_code=status.HTTP_200_OK)
async def get_result_for_test(test_id:int):
    res = []
    for result in results:
        if result.test_id == test_id:
            res.append(result)
    if res:
        return res
    raise HTTPException(status_code=404, detail="Test results not found!")
