'''
python.exeWrite a Python program to sort a list of elements using the bubble sort                                
Algorithm.
'''



def bubble_sort(xlist):
    for i in range(len(xlist)-1,0,-1):
        for j in range(i):
            if xlist[j] > xlist[j+1]:
                temp = xlist[j]
                xlist[j] = xlist[j+1]
                xlist[j+1] = temp


xlist = [5,3,8,6,7,2]
bubble_sort(xlist)
print(xlist)
