# 28. Write a Python program to find the second largest number in a list.

def second_largest(listx):
    listx.sort()
    if listx[-1] == listx[-2]:
        return listx[-3]
    else:
        return listx[-2]

print("Second largest element : ",second_largest([13,53,6,35,32,76,s46,5]))
