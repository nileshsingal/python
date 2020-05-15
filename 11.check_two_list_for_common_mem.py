# 11. Write a Python function that takes two lists and returns True if
# they have at least one common member.


def check_list(list1,list2):
    count = 0
    for i in list1:
        if i in list2:
            count += 1
    if count > 0:
            print("True")
    else:
            print("False")
            
print(check_list([1,2,3,4,5],[9,6,7,8,1]))
