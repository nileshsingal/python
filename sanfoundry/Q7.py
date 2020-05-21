# Print all Numbers in a Range Divisible by a Given Number

def divisible(ln,hn):
    num = int(input("Enter number : "))
    for i in range(ln,hn+1):
        if i % num == 0:
            print(i)
divisible(1,50)
