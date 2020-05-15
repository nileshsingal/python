# 17. Write a Python program to generate and print a list except for the first 5 elements,
# where the values are square of numbers between 1 and 30 (both included). 

def squares():
    sq_list = []
    for i in range(1,31):
        sq_list.append(i ** 2)
    print(sq_list[6:])

squares()
