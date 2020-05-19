#How to create and call Method of a Class?

class Employee:
    salary = 2000000
    name = "Nilesh Singal"
 
    def tax(self):
        print(self.salary * 0.10)
 
 
emp1 = Employee()
print(emp1.salary)
print(emp1.name)
emp1.tax()
