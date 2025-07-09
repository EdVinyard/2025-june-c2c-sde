class Student:
    def __init__(self, id, name, grades):
        self.id = id
        self.name = name
        self.grades = list(grades)

    def grade_average(self):
        total = 0.0
        for grade in self.grades:
            total += float(grade)
        return total / float(len(self.grades))

class Classroom:
    def __init__(self):
        self.students = []

    def add(self, student):
        self.students.append(student)

    def remove(self, id):
        for student in self.students:
            if student.id == id:
                self.students.remove(student)

    def grade_average(self):
        total = 0
        for student in self.students:
            total += student.grade_average()
        return total / float(len(self.students))

classroom = Classroom()

classroom.add(Student(2, 'June Bug Jr.',  [80, 90, 100]))
classroom.add(Student(1, 'Frank the Cat', [70, 80, 90]))
classroom.add(Student(3, 'Double Bubble', [60, 70, 80]))

print(classroom.grade_average())
