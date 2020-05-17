'''
12. Write a Python function that checks whether a passed string is palindrome or not. 
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
'''

def is_palindrom(string):
    if string[:] == string[:: -1]:
        return True
    else:
        return False
print(is_palindrom("madam"))
    
