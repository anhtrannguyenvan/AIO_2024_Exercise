###Tu luan
##Cau2a
from typing import Any


class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    def describe(self):
        return f"Name: {self.name} - YoB: {self.yob}"


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        return f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}"
    
    
class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject
        
    def describe(self):
        return f"Teacher: Name={self.name}, Year of Birth={self.yob}, Subject={self.subject}"

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        return f"Doctor: Name={self.name}, Year of Birth={self.yob}, Specialist={self.specialist}"

#Examples
student1 = Student ( name =" studentA ", yob =2010 , grade ="7")
student1.describe()

teacher1 = Teacher ( name =" teacherA ", yob =1969 , subject =" Math ")
teacher1.describe()

doctor1 = Doctor ( name =" doctorA ", yob =1945 , specialist =" Endocrinologists ")
doctor1.describe()

print(student1.describe())
print(teacher1.describe())
print(doctor1.describe())

##Cau2
class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []
    
    def add_person(self, person):
        self.people.append(person)
    
    def describe(self):
        description = f"Ward Name: {self.name}\n"
        description += "People:\n"
        for person in self.people:
            description += person.describe() + "\n"
        return description
    def count_doctor(self):
        return sum(isinstance(person, Doctor) for person in self.people)
    #cau2c
    def sort_age(self):
        self.people.sort(key=lambda person:person.yob)
        
    ##cau2d
    def compute_average(self):
        teachers = [person for person in self.people if isinstance(person, Teacher)]
        if not teachers:
            return 0
        total_yob = sum(teacher.yob for teacher in teachers)
        return total_yob/ len(teachers)

        
    
#test case 2b
teacher2 = Teacher ( name =" teacherB ", yob =1995 , subject =" History ")
doctor2 = Doctor ( name =" doctorB ", yob =1975 , specialist =" Cardiologists ")
ward1 = Ward ( name =" Ward1 ")
ward1 . add_person ( student1 )
ward1 . add_person ( teacher1 )
ward1 . add_person ( teacher2 )
ward1 . add_person ( doctor1 )
ward1 . add_person ( doctor2 )
ward1 . describe ()
print(ward1 . describe ())
        
    
##test case 2c
print ("Number of doctors : ", ward1.count_doctor())

#testcase 2d
print("\nAfter sorting Age of Ward1 people:")
ward1.sort_age()
print(ward1.describe())

#testcase2e
print ("Average year of birth ( teachers ):" ,ward1 . compute_average ())







