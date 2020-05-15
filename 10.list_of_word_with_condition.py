# 10. Write a Python program to find the list of words that are longer than n from a given list of words. 

# Method 1

'''
sample_string = input("Enter sentence to check : ")
txt = sample_string.split( )
n = int(input("Enter word limit :"))
req_words = []
for word in txt:
    if len(word) > n:
        req_words.append(word)
print(req_words)
'''

# Method 2

def string_check(n,string):
    txt = string.split( )
    req_str = []
    for word in txt:
        if len(word) > n:
            req_str.append(word)
    return req_str

print(string_check(3,"i love to code in python than other languages "))
    
