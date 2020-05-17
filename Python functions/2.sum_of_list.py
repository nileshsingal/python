'''
2. Write a Python function to sum all the numbers in a list. 
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
'''

def sum_of_list(xlist):
    sumx = 0
    for element in xlist:
        sumx += element
    print(sumx)


sum_of_list([1,4,6,7])
