#Write a Python program for Binary search.


def BinarySearch(list1, key):

    low = 0
    high = len(list1)-1
    
    Found = False

    while low <= high and not Found:
        mid = (low + high) // 2

        if key == list1[mid]:
            Found = True
        elif key > list1[mid]:
            low = mid + 1
        else:
            high = mid - 1

    if Found == True:
        print("Key is found ")
    else:
        print("key is not found ")




list1 = [10,23,56,78,5,87,98,33]
list1.sort()
key = int(input("Enter key value :"))
print(list1)
BinarySearch(list1, key)

