'''
2. Write a Python program to count the number of even and odd numbers from                     a series of numbers.
Sample numbers :
 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4
'''


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,12,14,16,322,2,5,7,32,467,8431,234,2555]
even_cnt = 0
odd_cnt = 0
for i in numbers:
    if i % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1

print("Number of even numbers : ",even_cnt)
print("Number of odd numbers : ",odd_cnt)
