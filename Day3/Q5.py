'''
Write a Python program to check whether a given number is a narcissistic number
or not
For example, 371 is a narcissistic number;
it has three digits,
and if we cube each digits  3^3 + 7^3 + 1^3 the sum is 371.
Other 3-digit narcissistic numbers
are 
153 = 1^3 + 5^3 + 3^3  , 370 = 3^3 + 7^3 + 0^3,
 407 = 4^3 + 0^3 + 7^3.
 There are also 4-digit narcissistic numbers,
some of which are 1634, 8208, 9474 since 1634 = 1^4+6^4+3^4+4^4

'''

n = int(input("Please enter number to check :"))
o_no = n
r_no = 0

if len(str(n)) >  0:
    po = len(str(n))
    while n > 0:
        d = n % 10
        r_no += d ** po
        n = n // 10
if o_no == r_no:
    print(o_no,"is a narcissistic number")
else:
    print(o_no,"Not a narcissistic number")
    
    
    
    
