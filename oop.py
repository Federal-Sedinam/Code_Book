class Person:
    """
    Base, Parent class
    """
    def __init__(self, name="Human Being", age=200, height=90, weight=70):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        # Some complex logic
        ...
        print("I'm eating...")

    def walk(self):
        # Some complex logic
        ...
        print("I'm walking...")


class Student(Person):
    """
    Inheritance:
    Is a - relationship
    Child, Derived class
    """
    def __init__(self, id, course="CS", name="Human Being", age=200, height=90, weight=70):
        self.id = id
        self.course = course
        super().__init__(name, age, height, weight)

    def take_course(self):
        # Some complex logic
        ...
        print("Take the course...")


class School:
    """
    Composition:
    has a - relationship
    """
    def __init__(self, students: list[Student]) -> None:
        self.students = students