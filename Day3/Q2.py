'''
From a list containing ints, strings and floats,
make three lists to store them separately. 
'''

listx = ["shankar",23,10.2,"yamendra",24, 10.7]

str_list = []
int_list = []
float_list = []

for i in listx:
    if type(i) == int:
        int_list.append(i)
    elif type(i) == str:
        str_list.append(i)
    else:
        float_list.append(i)

print("Integer elements from prev list :",int_list)
print("String elements from prev list :",str_list)
print("float elements from prev list :",float_list)


