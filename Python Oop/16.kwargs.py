#Create multiple Class variables pass in argument list

'''
**kwargs is a dictionary of keyword arguments.
The ** allows us to pass any number of keyword arguments.
A keyword argument is basically a dictionary.

An example of a keyword argument is fun(foo=2,bar=7).

**kwargs are just like *args except you declare the variables and the amount within the function arguments.

'''

class Employee(object):
    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
 
 
emp = Employee(age=23, name="Nilesh Singal")
print(emp.age)
print(emp.name)
