# Student class
class Student:
    def __init__(self, sid, name, m1, m2, m3, birth, fee_paid):
        self.sid = sid
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.birth = birth
        self.fee_paid = fee_paid
        self.total_fee = 50000

    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def cgpa(self):
        return self.average() / 10

    def age(self):
        return 2026 - self.birth

    def fee_balance(self):
        return self.total_fee - self.fee_paid


# College class
class College:
    def __init__(self, code, name, location):
        self.code = code
        self.name = name
        self.location = location
        self.students = []

    def register(self, s):
        self.students.append(s)

    def display(self):
        print("College:", self.name, "-", self.location)
        for s in self.students:
            print("\nStudent ID:", s.sid)
            print("Name:", s.name)
            print("CGPA:", round(s.cgpa(),2))
            print("Age:", s.age())
            print("Fee Balance:", s.fee_balance())


# Create college
c = College("C101", "ANITS", "Visakhapatnam")

# Register 3 students
s1 = Student(1, "Abhishek", 85, 80, 90, 2005, 30000)
s2 = Student(2, "Rahul", 75, 70, 80, 2004, 35000)
s3 = Student(3, "Kiran", 88, 92, 84, 2005, 40000)

c.register(s1)
c.register(s2)
c.register(s3)

# Display report
c.display()