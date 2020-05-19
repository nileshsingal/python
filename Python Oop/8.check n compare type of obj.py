#How to check and compare type of an object?

'''
Class, or type, is an object that holds information about how to construct
a certain kind of objects and what that kind of objects can do. A type is
the class of a class. Like everything else in Python, classes themselves
are objects, and you can pass them around, assign them to variables, etc.
If you ask a class what its class is, you will get the answer type.
If you ask a class instance what its class is, you will of course get the class.

'''

class Test(object):
    pass
 
 
print(type(Test))
 
obj1 = Test()
print(type(obj1))
 
obj2 = Test()
print(type(obj1) is type(obj2))
