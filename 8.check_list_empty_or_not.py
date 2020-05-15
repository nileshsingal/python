# 8. Write a Python program to check a list is empty or not.

# Method 1
'''
listx = [1]
if len(listx) > 0:
    print("True")
else:
     print("False")
'''

# Method 2

def check_list(xlist):
    if len(xlist) > 0:
        return True
    else:
        return False

print(check_list([1,2]))
