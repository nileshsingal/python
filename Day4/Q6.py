'''
Write a program to obtain the sum of the first and last digit of this number 2 user defined functions
1st for first digit
2nd for last digit
Example:
 Input:  5424
Output: 9
'''

def sum_first_last_digit(n):

    string_num = str(n)
    f_digit = int(string_num[0])
    l_digit = int(string_num[-1])

    print(f_digit + l_digit)
    
    

sum_first_last_digit(5424)
