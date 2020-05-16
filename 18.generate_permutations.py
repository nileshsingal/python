# 18. Write a Python program to generate all permutations of a list in Python. 


from itertools import permutations

perm = permutations([1,2,3])

for i in list(perm):
    print(i)
    
