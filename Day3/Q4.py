
# 4.Accept data in two 3*3  matrix and calculate the sum of the matrices.
a = [[1,1,1],
    [1,1,1],
    [1,1,1]]

b = [[1,2,3],
    [4,5,6],
    [7,8,9
     ]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]


for i in range(len(a)):
   
   for j in range(len(a[0])):
       result[i][j] = a[i][j] + b[i][j]

for r in result:
   print(r)
