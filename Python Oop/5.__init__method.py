#How to use the __init__() method to assign values to data attributes?

'''
Python classes have a special method named __init__ which is automatically
executed when an instance of the class is created in memory.
'''


class Employee:
        def __init__(self, salary, name):
                self.salary = salary
                self.name = name
 
 
emp1 = Employee(10000, "Nilesh Singal")
print(emp1.salary)
print(emp1.name)


'''
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def tax(self):
        print(self.salary * 0.10)

e1 =Employee("nilesh singal",2000000)
print(e1.name)
print(e1.salary)
e1.tax()
'''
