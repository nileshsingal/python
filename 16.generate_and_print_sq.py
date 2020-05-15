# 16. Write a Python program to generate and print a list of first and last 5 elements
# where the values are square of numbers between 1 and 30 (both included).

# Method 1
'''

square = []
for i in range(1,31):
    sq = i ** 2
    square.append(sq)
print(square[:5])
print(square[-5:])


'''

# Method 2

def req_square():
    req_list = []
    for i in range(1,31):
        req_list.append(i ** 2)
    print(req_list[:5])
    print(req_list[-5:])

req_square()
