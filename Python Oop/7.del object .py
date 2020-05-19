#How to Delete object properties and object?


class Employee:
    def __init__(self, salary, name):
        self.salary = salary
        self.name = name
 
 
emp1 = Employee(100000, "Nilesh Singal")
 
del emp1.salary     # Delete object property
del emp1            # Delete object
 
