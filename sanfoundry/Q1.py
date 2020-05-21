#Calculate the Average of Numbers in a Given List

n = int(input("Enter number : "))

a = []


for i in range(n):
    num = int(input("Enter number in list: "))
    a.append(num)
avg = sum(a) / n
print(avg)
    
