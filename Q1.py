# 1. Write a Python program to sum all the items in a list.

# Method 1

list1 = [10,20,30,40,50]
print(sum(list1))


# Method 2
'''
list1 = [10,20,30,40,50]
xsum = 0 
for i in list1:
    xsum += i
print(xsum)
'''

# Method 3
'''

def add_list_elements(listx):
    xsum = 0
    for i in listx:
        xsum += i
    print(xsum)

sample = [10,20,30,40,50]
add_list_elements(sample)
'''

#Method 4
'''
def add_list_elements(listx):
    return sum(listx)

print(add_list_elements([10,20,30,40,50]))
'''
