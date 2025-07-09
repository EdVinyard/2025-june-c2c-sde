class Student:
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade

    def update_grade(self, new_grade):
        self.grade = new_grade

    def __str__(self):
        return f'{self.id} {self.name} {self.grade}'

frank = Student(123, 'Frank the Cat', 78.0)
print(frank)
frank.update_grade(84.0)
print(frank)
