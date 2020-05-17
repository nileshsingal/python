'''
3. Write a Python function to multiply all the numbers in a list. 
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336

'''

def mul_list(xlist):
    mul = 1
    for i in xlist:
        mul *= i
    return mul

print(mul_list([1,3,9,4,6]))
