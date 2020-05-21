#Print Odd Numbers Within a Given Range

l_limit = int(input("initilize lower limit :"))
u_limit = int(input("initilize upper limit :"))

for i in range(l_limit,u_limit+1):
    if i % 2 != 0:
        print(i)
