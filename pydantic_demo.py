from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'Tanya'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the CGPA of the student')

new_student = {'age': '26', 'email': 'abc@gmail.com'}

student = Student(**new_student)

print(student)

print(student.age)

print(type(student.age))

student_dict = dict(student)
student_json = student.model_dump_json

print(student_dict['age'])
print(student_json)