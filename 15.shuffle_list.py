#15. Write a Python program to shuffle and print a specified list. 



#Method 1

import random

listx = [1,2,3,4,5,6,7,8,9]
print("Original list : ", listx)
random.shuffle(listx)
print("Shuffled list : ", listx)




#Method 2

'''

import random

def shuffled_list(xlist):
    random.shuffle(xlist)
    return xlist

print("shuffled list : ",shuffled_list([1,2,3,4,5,6]))
    

'''
