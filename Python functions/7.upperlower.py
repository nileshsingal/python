'''
7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
'''


def upperlower(string):
    upper = 0
    lower = 0

    for i in range(len(string)):
        if ord(string[i]) >= 97 and ord(string[i]) <= 122:
            lower += 1

        elif ord(string[i]) >= 65 and ord(string[i]) <= 90:
            upper += 1

    print('Lower case characters = %s' %lower)
    print('Upper case characters = %s' %upper)

string = "Hi How Are You Doing"
upperlower(string)
  
