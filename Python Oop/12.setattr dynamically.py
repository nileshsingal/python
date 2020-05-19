#How to create Data Attributes of a class dynamically?

'''
The setattr used to sets the named attribute on the given object with a specified
value.
'''

class Employee:
    pass
 
 
emp1 = Employee()
setattr(emp1, 'Salary', 12000)
 
emp2 = Employee()
setattr(emp2, 'Age', 25)
 
print(emp1.Salary)
print(emp2.Age)
