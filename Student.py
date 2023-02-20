class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Student("Isko Abelardo", 21)
p2 = Student("SADBOYS", 2001)

print("Name: " + p1.name)
print("Age: " + str(p1.age))
print("Name: " + p2.name)
print("Age: " + str(p2.age))
