# 29. Write a Python program to get unique values from a list. 


def unique_values(xlist):
    xset = set(xlist)
    xlist = list(xset)
    print("Unique elements : ",xlist)

unique_values([1,3,5,6,8,4,12,3,4,5,6,8,8,3,1,35,7,8,5,3,1])
