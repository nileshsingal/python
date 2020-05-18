# 10. Write a Python program to issubset and issuperset. 

A = {1, 2, 3, 4, 5}
B = {1, 2, 3}

# Set A is said to be the superset of set B if all elements of B are in A.

# Returns True
print(A.issuperset(B))

# Returns False
print(B.issuperset(A))

