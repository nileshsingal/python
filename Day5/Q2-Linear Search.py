#2 Write a Python program for sequential search (Linear search).

pos = -1

def linear_search(xlist,n):
    i = 0

    while i < len(xlist):
        if xlist[i] == n:
            globals() ['pos'] = i
            return True
        i = i + 1
        
    return False

xlist = [5,8,4,6,9,2]
n = 9

if linear_search(xlist,n):
    print("Found at ", pos+1)
else:

    print("Not found")
