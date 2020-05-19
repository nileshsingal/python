'''
6. Write a Python program to square and cube every number
in a given list of integers using Lambda.
'''

def sq_cu(xlist):
    square = []
    cube = []
    for x in xlist:
        square.append(x ** 2)
        cube.append(x ** 3)
    print("square is :",square)
    print("Cube is : " ,cube)

sq_cu([1,2,3,4,5])


