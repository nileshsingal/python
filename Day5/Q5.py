'''
⦁Iterate a given list and check if a given element already exists in a
dictionary as a key’s value if not delete it from the list.
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sampledict = {“John”:47,”Peter”:64,”Mahi”:37,”Maria”:76}
'''

roll_no = [47, 64, 69, 37, 76, 83, 95, 97]
sampledict = {"Shankar": 64,"yamendra":97,"nilesh":78}
result = [i for i in roll_no if i in sampledict.values()]
print(result)
