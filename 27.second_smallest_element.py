#27. Write a Python program to find the second smallest number in a list.

def smallest_num(list1):
    list1.sort()
    print("Second Smallest element in list : ")
    if list1[0] == list1[1]:
        return list1[2]
    else:
        return list1[1]

print(smallest_num([4,6,8,5,3,6,8,90,]))
