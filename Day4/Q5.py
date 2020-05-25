'''
Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [11,22,22,33,33,33,44,55,55,66]
Unique List : [11, 22,33, 44, 55,66]
'''


def unique_list(xlist):
    xset = set(xlist)
    xlist = set(xset)
    print(xlist)

unique_list([1,1,2,2,45,4,6,7,6,45,98,45,456])
