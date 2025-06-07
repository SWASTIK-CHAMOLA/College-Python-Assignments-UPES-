# 1. Create a Class of Student
class Student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks  # [phy, chem, maths]

    def display(self):
        print("Name:", self.name)
        print("SAP ID:", self.sap_id)
        print("Marks (Physics, Chemistry, Maths):", self.marks)
        print("-" * 30)

# Creating 3 student objects with user input
students = []

for i in range(3):
    print(f"Enter details for Student {i + 1}")
    name = input("Enter name: ")
    sap_id = input("Enter SAP ID: ")
    phy = int(input("Enter Physics marks: "))
    chem = int(input("Enter Chemistry marks: "))
    maths = int(input("Enter Maths marks: "))
    marks = [phy, chem, maths]
    student = Student(name, sap_id, marks)
    students.append(student)
    print()

# Display details
print("\n--- Student Details ---\n")
for student in students:
    student.display()


# 2. Add Constructor and Methods
class Student:
    def __init__(self, name, sap_id, phy, chem, maths):
        self.name = name
        self.sap_id = sap_id
        self.phy = phy
        self.chem = chem
        self.maths = maths

    def display(self):
        print(f"Name: {self.name}, SAP ID: {self.sap_id}, Marks: {self.phy}, {self.chem}, {self.maths}")

    def find_marks_percentage(self):
        return ((self.phy + self.chem + self.maths) / 300) * 100

    def display_result(self):
        if self.phy >= 40 and self.chem >= 40 and self.maths >= 40:
            return "Pass"
        else:
            return "Fail"

# Input for n students
n = int(input("Enter number of students: "))
students = []
for i in range(n):
    print(f"\nStudent {i+1}")
    name = input("Name: ")
    sap_id = input("SAP ID: ")
    phy = int(input("Physics Marks: "))
    chem = int(input("Chemistry Marks: "))
    maths = int(input("Maths Marks: "))
    students.append(Student(name, sap_id, phy, chem, maths))

# Display details and results
total_percent = 0
print("\nDetails and Result:")
for s in students:
    s.display()
    percent = s.find_marks_percentage()
    total_percent += percent
    print(f"Percentage: {percent:.2f}%")
    print(f"Result: {s.display_result()}")
    print("---------------------------")

# Class average
class_avg = total_percent / n
print(f"Class Average Percentage: {class_avg:.2f}%")


# 3. Implement Different Types of Inheritance
s = Student("Prakhar")
s.display()

class A:
    def showA(self):
        print("This is Class A")

class B(A):
    def showB(self):
        print("This is Class B")

class C(B):
    def showC(self):
        print("This is Class C")

obj = C()
obj.showA()
obj.showB()
obj.showC()

class Father:
    def skills(self):
        print("Gardening, Driving")

class Mother:
    def skills(self):
        print("Cooking, Painting")

class Child(Father, Mother):
    def more_skills(self):
        print("Coding")

c = Child()
c.skills()  # Will call Father's skills due to MRO
c.more_skills()


# 4. Implement Method Overriding
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()
d.sound()


# 5. Operator Overloading for Adding Point Objects
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def display(self):
        print(f"Point({self.x}, {self.y})")

P1 = Point(10, 20)
P2 = Point(12, 15)
P3 = P1 + P2
P3.display()
