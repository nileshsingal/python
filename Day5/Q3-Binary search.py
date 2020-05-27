#Write a Python program for Binary search.

pos = -1
def binarySearch(xlist,n):
    l = 0
    u = len(xlist)-1

    while l <= n:
        
        mid = (l + u) // 2
    
        if xlist[mid] == n:
            globals() ['pos'] = mid
            return True
        else:
            if xlist[mid] < n:
                l = mid
            else:
                u = mid

xlist=[7,12,34,45,76]

n = 45

if binarySearch(xlist, n):
    print("Found at :", pos+1)
else:
    print("Not Found")
