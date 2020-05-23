'''
  4.Given the triangle of consecutive odd  numbers
		                 
Above triangle is given Calculate Sum row wise 

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29

Example we call function :- row_sum_odd_numbers(2)
Result will be=3 + 5 = 8
if user give 4 then ur output is13 + 15 + 17+ 19 = 64
'''

def row_sum(n):
    return n * n * n
print(row_sum(4))
