# 20. Write a Python program access the index of a list.

# Method 1

'''

testlist = [1,2,3,4,5,6,7,8]

print("original list is : ",str(testlist))

print("List index-value are : ")
for i in range(len(testlist)):
    print(i,testlist[i])

'''

# Method 2 -> using List comprehenshion

'''

testlist = [1,2,3,4,5,6,7,8]

print("original list is : ",str(testlist))

print("List index-value are : ")

print([list((i, testlist[i])) for i in range(len(testlist))])

'''




# Method 3 : Using enumerate()

test_list = [1, 4, 5, 6, 7]
print ("Original list is : " + str(test_list))

print ("List index-value are : ")
for index, value in enumerate(test_list):
    print(index , value)




# Method 4 : Using zip()

'''

test_list = [1, 4, 5, 6, 7]
print ("Original list is : " + str(test_list))
print ("List index-value are : ")
for index, value in zip(range(len(test_list)), test_list): 
    print (index, value)

'''

