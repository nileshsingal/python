# Python Program to Read a Number n And Print the Series “1+2+…..+n= “
n = int(input("Enter number :"))
a = []
for i in range(1,n+1):
    print(i,sep=" ",end=" ")
    a.append(i)
    if i < n:
        print("+",sep=" ",end=" ")
print("=",sum(a))
