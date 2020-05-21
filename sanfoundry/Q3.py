# Read a Number n and Compute n+nn+nnn

n = int(input("Enter number : "))
d = 0
r = 0
add = 0
for i in range(1,4):
    d = n
    r = (r * 10) + d
    add += r

print(add)
    
