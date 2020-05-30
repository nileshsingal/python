

#Python program to Swap Keys and Values in Dictionary.


Dict={"Name":"Nilesh","age":23,"id":22,"Address":"Chatrapati Sambhaji nagar" }

s_Dict={}

for key,value in Dict.items():
    if key in Dict:
        s_Dict[value]=key
    else:
        s_Dict[value]=key
        
print(s_Dict)
