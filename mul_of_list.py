# 2. Write a Python program to multiplies all the items in a list. 

# Method 1
'''
list1 = [10,20,30,40,50]
mul = 1
for i in list1:
    mul *= i
print(mul)
'''

# Method 2

def mul_list(xlist):
    mul = 1
    for i in xlist:
        mul *= i
    print(mul)

mul_list([10,20,30,40,50])
        
