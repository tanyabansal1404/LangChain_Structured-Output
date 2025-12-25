from pydantic import BaseModel

class Student(BaseModel):

    name: str

new_student = {'name': 'Tanya'}

student = Student(**new_student)

print(student)

print(type(student))