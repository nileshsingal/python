#How to update Object properties in Python?

class Employee:
    def __init__(self, salary, name):
        self.salary = salary
        self.name = name
 
 
emp1 = Employee(100000, "Nilesh Singal")
print(emp1.salary)
 
emp1.salary = 200000
print(emp1.salary)
