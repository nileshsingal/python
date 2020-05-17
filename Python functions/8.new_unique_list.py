'''
8. Write a Python function that takes a list and returns a new list with unique elements of the first list. 
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]

'''
def remove_dup(listx):
    unique_list = set(listx)
    return unique_list

print(remove_dup([1,22,3,4,5,3,2,1,3,4,5,3,1,12,3,4,5]))
    
