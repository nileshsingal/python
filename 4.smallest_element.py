# 4. Write a Python program to get the smallest number from a list. 

# Method 1
'''
listx = [11,26,86,47,28,39,48,27,8,38]
print("Minimun Element present in list is : ", min(listx))
'''

# Method 2
'''
listx = [11,26,86,47,28,39,48,27,8,38]
listx.sort()
print("Minimun Element present in list is : ", listx[0])
'''

# Method 3

def min_element_frm_list(listx):
    print("Minimun Element present in list is : ", min(listx))

min_element_frm_list([56,47,8,36,9,36,5,24])
