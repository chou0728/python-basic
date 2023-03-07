from person import Person

# 繼承 Person


class Student(Person):
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

    def print_school(self):
        print(self.school)
