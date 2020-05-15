#3. Write a Python program to get the largest number from a list. 

# Method 1
'''
listx = [1,4,8,9,3,4,5,7,8,28,96,47]
print(max(listx))
'''
# Method 2

listx = [1,4,8,9,3,4,5,7,8,28,96,47]

listx.sort()
print(listx[-1])
