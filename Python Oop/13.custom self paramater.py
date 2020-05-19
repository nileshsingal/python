#How to create and use custom Self parameter?
'''
self is an object reference to the object itself,
it does not have to be named self ,
but it has to be the first parameter of any function in the class.
'''

class Employee:
    def __init__(person, salary, name):
        person.salary = salary
        person.name = name
 
    def print_details(emp):
        print(str(emp.salary) + ' : ' + emp.name)
 
 
emp1 = Employee(100000, 'Nilesh Singal')
emp1.print_details()
