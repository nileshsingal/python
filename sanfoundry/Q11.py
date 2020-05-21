#Find the Sum of Digits in a Number
n = int(input("Enter number : "))
r = 0
while n > 0:
    d = n % 10
    r += d
    n = n // 10

print(r)
