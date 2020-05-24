'''
You are given with a list of integer elements.
Make a new list which will store square of elements of previous list.
'''

prev_list = [4,7,9,23,14,65,78,8]
new_list = []

for i in prev_list:
    new_list.append(i ** 2)

print(new_list)
