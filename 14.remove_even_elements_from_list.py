# 14. Write a Python program to print the numbers of a specified list after
#removing even numbers from it.


def remove_even_frm_list(xlist):
    req_list = []
    for i in xlist:
        if i % 2 != 0:
            req_list.append(i)
    return req_list

print(remove_even_frm_list([12,3,45,64,78,83,25,7,4,9,63]))
