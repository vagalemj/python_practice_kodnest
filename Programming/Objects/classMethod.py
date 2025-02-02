class Student:
    college = "Presidency University"
    @classmethod
    def setCollege(cls, new_college):
        cls.college = new_college

Student.setCollege("Presidency School")
s1 = Student()
print(s1.college) # Presidency School