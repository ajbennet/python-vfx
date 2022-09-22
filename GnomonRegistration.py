# Represents any Gnomon person.
class Gnomie:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print(f"Initialized Gnomie for: {self.name}")

    # print
    def printGnomie(self):
        print(f"Name: {self.name} Age: {self.age} Gender: {self.gender}")


# Represents a Gnomie teacher.
class Teacher(Gnomie):
    def __init__(self, name, age, gender, contract):
        Gnomie.__init__(self, name, age, gender)
        self.contract = contract
        print(f"Initialized Teacher: {self.name}")

    def printGnomie(self):
        Gnomie.printGnomie(self)
        print(f"Salary: {self.contract}")


# Represents a Gnomie student.
class Student(Gnomie):
    def __init__(self, name, age, gender, program):
        Gnomie.__init__(self, name, age, gender)
        self.program = program
        print(f"Initialized Student: {self.name}")

    def printGnomie(self):
        Gnomie.printGnomie(self)
        print(f"Marks: {self.program}")


class CourseRegistration:
    def __init__(self, student, teacher, course):
        self.student = student
        self.teacher = teacher
        self.course = course
        print(f"Registration for: {self.student.name} with teacher: {self.teacher.name} for course: {self.course} complete")


if __name__ == '__main__':
    sowmini = Student("Sowmini", 12, "Female", "DP")
    sowmini.printGnomie()
    coldon = Teacher ("Coldon", 30, "Male", "FullTime")
    coldon.printGnomie()
    CourseRegistration(sowmini, coldon, "Python")
    print('Completed')
