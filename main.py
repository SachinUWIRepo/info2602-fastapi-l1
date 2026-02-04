from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
def hello_world():
    return 'Hello, World!'

# #This is a new function
# @app.get('/students')
# async def get_students():
#     return data
# #End of the new function

#Another Function
@app.get('/students/{id}')
async def get_student(id):
    for student in data:
        if student['id'] == id: #this only returns the student if the id matches
            return student
#End of the Other Function

#Get this the third Function
@app.get('/students')
async def get_students(pref=None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref: # select only the students with a given meal preference
                filtered_students.append(student) # add match student to the result
        return filtered_students
    return data
#End of the third function

@app.get('/statistics')
async def get_statistics():
    statistics = {}

    students = data

    # If data.json is a dictionary (not a list), try to extract students list
    if isinstance(data, dict):
        students = data.get('students', [])

    for student in students:
        pref = student.get('pref')
        programme = student.get('programme')

        if pref:
            statistics[pref] = statistics.get(pref, 0) + 1

        if programme:
            statistics[programme] = statistics.get(programme, 0) + 1

    return statistics



#Add Function
@app.get('/add/{a}/{b}')
async def add(a: int, b: int):
    return a + b
#End of Add Function

#Subtract Function
@app.get('/subtract/{a}/{b}')
async def subtract(a: int, b: int):
    return a - b
#End of Subtract Function

#Multiply Function
@app.get('/multiply/{a}/{b}')
async def multiply(a: int, b: int):
    return a * b
#End of Multiply Function

#Divide Function
@app.get('/divide/{a}/{b}')
async def divide(a: int, b: int):
    if b == 0:
        return 'Error: cannot divide by zero'
    return a / b
#End of Divide Function
