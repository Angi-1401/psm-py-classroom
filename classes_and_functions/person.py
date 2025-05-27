class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greating(self, name, age):
        print("Hola, soy ", name, " y tengo ", age, " años")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print("What I am doing with my life? :'v")


class Teacher(Person):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id

    def complain(self):
        print("I am not getting enough money for this -.-")


teacher = Teacher("Julio", "42", "123")
