# 9. Write a Python program to clone or copy a list.

# Method 1

'''
list1 = [1,2,3,4,5,6,7,8,9,10]
cloned_list = list1.copy()
print("Cloned list is :", cloned_list)

'''

# Method 2

def cloned_list(listx):
    cloned_list = listx.copy()
    print("Copy of listx is :",cloned_list)
cloned_list([1,2,3,4,5])
