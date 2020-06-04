
# Write a program to implement Constructor with Variable Number of Arguments.

class Timepass:
    def __init__(self,*args):
        print(sum(args))

t1 = Timepass(12,34,56,78)
t2 = Timepass(2,4,6,8,10)

# **kwargs keyword arguments

class Timepass2:
    def __init__(self,**kwargs):
        for i, j in kwargs.items():
            print(i,":",j)

ta = Timepass2(a = 17, b = 23)
