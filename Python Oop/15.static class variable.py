# How to create Static Class variables?

'''
Variables declared inside the class definition,
but not inside a method are class or static variables.
'''

class Employee:
    age = 25

print(Employee.age)

e = Employee()
print(e.age)

e.age = 30
print(Employee.age)     # 25
print(e.age)            # 30
