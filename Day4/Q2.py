#Write a Python program to detect the number of local variables declared in a function.

def cnt_local_var():
    x = 10
    y = 20
    fname = "nilesh"
    lname= "singal"
    age = 23

    print("Local Variabe present :",cnt_local_var.__code__.co_nlocals)

cnt_local_var()
    
