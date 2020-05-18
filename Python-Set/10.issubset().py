#10. Write a Python program to issubset and issuperset. 
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}


# if all the values of A is present in B then A is subset of B and returns True
print(A.issubset(B))

# if all values of B are not present in A then B is not subset of A and return False
print(B.issubset(A))
