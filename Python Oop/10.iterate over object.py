#How to Iterate over object attributes?
'''
Calling dir on the object gives you back all the attributes of that object,
including python special attributes.You can always filter out the special methods
by using a list comprehension.
'''

class A():
    m = 1
    n = 2

    def __init__(self, x=1, y=2, z=3):
        self.x = x
        self._y = y
        self.__z__ = z


    def xyz(self):
        print(x, y, z)

obj = A()
print(dir(obj))
print([a for a in dir(obj) if not a.startswith('__')])
