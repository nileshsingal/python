'''
Write a python program to concatenate two lists index-wise.
List1 = [“M”,”na”,”i”,”lak”]
List2 = [“y”,”me”,”s”,”han”]
Expected output:
[“My”,”name”,”is”,”lakhan”]
'''

list1 = ['M','Na','i','Lak']
list2 = ['y','me','s','han']

result = [(i+j) for i, j in zip(list1, list2)]
print(result)
