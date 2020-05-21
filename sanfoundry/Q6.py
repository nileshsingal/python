# Take in the Marks of 5 Subjects and Display the Grade
def calc_grade(m1,m2,m3,m4,m5):
    tsum = m1 + m2 + m3 + m4 + m5
    div = 5
    avg = tsum / 5

    if avg >= 90:
        print("grade A")
    elif 90 >= avg <= 80:
        print("Grade B")
    elif 60 <= avg >= 70:
        print("Grade C")
    elif avg >= 35:
        print("grade D")
    else:
        print("Fail")

calc_grade(20,30,40,75,30)
