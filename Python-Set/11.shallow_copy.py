#11. Write a Python program to create a shallow copy of sets.
'''
A shallow copy constructs a new compound object and then
(to the extent possible) inserts references into it to the objects
found in the original.
'''


import copy
set1 = {"one","two","three"}
#shallow copy
shallow_copy = copy.copy(set1)
print(shallow_copy)
