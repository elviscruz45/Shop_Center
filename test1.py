class Student:
    count = 0
    def __init__(self):
        Student.count += 1




std1=Student()

print(std1.count)

print("------------------------")

std1=Student()
std1=Student()
std1=Student()
std1=Student()
std1=Student()

print(Student.count)
print(Student.count)
print(Student.count)
print(Student.count)
print(Student.count)
