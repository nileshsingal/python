# 6. Write a Python function to check whether a number is in a given range.

def check_range(n):
    if n in range(3,9):
        print("The Number ",n," is in given range")
    else:
        print("The Number ",n," is not in given range")

check_range(7)
