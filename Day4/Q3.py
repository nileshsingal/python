'''
Write a recursive function to calculate the sum of numbers from 0 to 10
Expected output: 55
'''


def rec_add(n):
    if n == 1:
        return 1
    else:
        return n + rec_add(n-1)

print(rec_add(10))
    
