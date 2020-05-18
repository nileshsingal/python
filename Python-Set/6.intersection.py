# 6. Write a Python program to create an intersection of sets.

# usinf for loop
'''

set1 = {1,2,3,4,5,6}
set2 = {5,6,7,8,9,10}
intersection = set()

for i in set1:
    for j in set2:
        if i == j:
            intersection.add(i)
print(intersection)
'''

# using (&->means intersection)

set1 = {1,2,3,4,5,6}
set2 = {5,6,7,8,9,10}
result = set1 & set2
print(result)
