from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {'name': 'X','age': '11'}

print(new_person)