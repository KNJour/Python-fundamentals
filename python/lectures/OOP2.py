class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

class Dojo:
    def __init__(self, course_name, max_students, instructor):
        self.course_name = course_name
        self.max_students = max_students
        self.instructor = instructor
        self.num_of_students = []


    def add_student(self, student):
        if len(self.num_of_students) < self.max_students:
            self.num_of_students.append(student)
        else:
            print("This class is at maximum capacity. Can not add")
        return self
        

    def display_students(self):
        for student in self.num_of_students:
            print(f"Student Name: {student.name}, Student Grade: {student.grade}")
        return self
    def update_grade(self, student, new_grade):
        student.grade = new_grade
        return self

student1 = Student("Bruce Wayne", 21, 90)
student2 = Student("Robin", 18, 50)
student3 = Student("Ghost Rider", 40, 75)

course1 = Dojo("Crime fighting class", 3, "Superman")

course1.add_student(student1)
course1.add_student(student2)
course1.add_student(student3)

course1.display_students()

# course1.update_grade(student1, 70)

print 