#1 Write a function to compute divide by zero and use try/except to catch the exceptions.



def divide(num1, num2):
    try:
        result = num1 / num2
        print("result : ", result)
    except Exception as arg:
        print("Exception raised : ", arg)
    finally:
        print("End of program ")


num1 = int(input("Enter 1st num : "))
num2 = int(input("Enter 2st num : "))
divide(num1, num2)
