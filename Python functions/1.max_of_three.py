# 1. Write a Python function to find the Max of three numbers. 

def max_of_three(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        print(n1," is max ")
    elif n2 > n1 and n2 > n3:
        print(n2," is max ")
    else:
        print(n3, "is max ")

max_of_three(12,45,7)
