#Count the Number of Digits in a Number
num = int(input("Enter number :"))
digit = 0
while num > 0:
    d = num % 10
    digit += 1
    num = num // 10
print(digit)
