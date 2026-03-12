# Personal information class
class PersonalInfo:
    def __init__(self, name, dob, phone, email):
        self.name = name
        self.dob = dob
        self.phone = phone
        self.email = email

    def show_personal(self):
        print("Name:", self.name)
        print("DOB:", self.dob)
        print("Phone:", self.phone)
        print("Email:", self.email)


# Education class
class Education(PersonalInfo):
    def __init__(self, name, dob, phone, email, degree, university, year, cgpa):
        PersonalInfo.__init__(self, name, dob, phone, email)
        self.degree = degree
        self.university = university
        self.year = year
        self.cgpa = cgpa

    def show_education(self):
        print("Degree:", self.degree)
        print("University:", self.university)
        print("Graduation Year:", self.year)
        print("CGPA:", self.cgpa)


# Experience class
class Experience(Education):
    def __init__(self, name, dob, phone, email, degree, university, year, cgpa,
                 company, role, exp, skills):
        Education.__init__(self, name, dob, phone, email, degree, university, year, cgpa)
        self.company = company
        self.role = role
        self.exp = exp
        self.skills = skills

    def show_experience(self):
        print("Company:", self.company)
        print("Role:", self.role)
        print("Experience:", self.exp, "years")
        print("Skills:", self.skills)


# Candidate Profile class
class CandidateProfile(Experience):
    def display_profile(self):
        self.show_personal()
        self.show_education()
        self.show_experience()

        if self.exp > 5:
            print("Eligible for: Senior Role")
        else:
            print("Eligible for: Junior Role")
        print("---------------------------")


# Candidate objects
c1 = CandidateProfile("Rahul", "10-05-1998", "9876543210", "rahul@gmail.com",
                      "B.Tech", "ANITS", 2021, 8.5,
                      "TCS", "Developer", 6, "Python, SQL")

c2 = CandidateProfile("Kiran", "15-08-2000", "9876501234", "kiran@gmail.com",
                      "B.Tech", "ANITS", 2022, 8.2,
                      "Infosys", "Tester", 3, "Java, Testing")

# Display profiles
c1.display_profile()
c2.display_profile()
