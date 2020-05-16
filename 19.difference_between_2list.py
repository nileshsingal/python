# 19. Write a Python program to get the difference between the two lists

#Method 1

'''

list1 = [10,20,30,40,50]
list2 = [10,50]

print(set(list1) - set(list2))

'''

#Method 2

def Diff(li1, li2): 
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
    return li_dif 

li1 = [10, 15, 20, 25, 30, 35, 40] 
li2 = [25, 40, 35] 
li3 = Diff(li1, li2) 
print(li3) 
