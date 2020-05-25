'''
Create a function showStudent() in such a way that it should
accept student id, name, and it’s college name  and if the id
and college name is missing in function call it should show it as by default
id is 1 and college name  is VITA.
'''

def showStudent(s_name,s_id = 1,c_name = "VITA"):
    print (" student_id :",s_id,"\n", "student_name :",s_name,"\n","college name :",c_name)

showStudent("nilesh")
