import Student
import Grades

p1 = Student.Student("Isko Abelardo", 21)
p2 = Grades.Grades("CPE028", 3, 100)

print("Name: " + p1.name)
print("Age: " + str(p1.age))
print("Course Code: ", p2.Course_Code)
print("Course Units: ", p2.Course_Units)
print("Course Grade: ", p2.Course_Grade)