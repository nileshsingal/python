'''
Write python program to perform bank operations using class and objects.


Conditions:
            a. Bank name should be static.
            b. Using menu driven program.

                1 .Deposit
                2. Withdraw
                3. Exit
'''

import sys
class Customer:
    bankName = "State Bank Of India"

    def __init__(self,name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("balance is :", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance please enter less amount than balance amount")
            sys.exit()
        self.balance -= amount
        print("Remaining balance is : ", self.balance)
print("Welcome to %s....How may I help You."%(Customer.bankName))
name = input("Please Enter Your Name :")
c = Customer(name)

while True:
    print("Enter Transaction:\n1.Withdrawal\n2.Deposit\n3.Exit")
    option = int(input("Please select an option :"))
    if option == 1:
        amount = float(input("Enter amount to withdraw :"))
        c.withdraw(amount)
    elif option == 2:
        amount = float(input("Enter amount to Deposite in bank : "))
        c.deposit(amount)
    elif option == 3:
        print("Thank you, Visit Again !!!")
        break
    else:
        print("Invalid Option selected plz try with another option.")
