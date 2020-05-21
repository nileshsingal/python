#Check if a Number is a Palindrome

n = int(input("Enter number :"))
o_no = n
r_no = 0
while n > 0:
    d = n % 10
    r_no = (r_no * 10) + d
    n = n // 10

if r_no == o_no:
    print(o_no," : is palindrome number")
else:
    print(o_no, " : is Not a palinfrome number" )
