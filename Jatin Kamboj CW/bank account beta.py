#Bank Account
#By Jatin Kamboj
class bankaccount(object):
    def __init__(self,amt):
        self.balance=amt
    def deposit(self,amt):
        self.balance+=amt
    def withdraw(self,amt):
        self.balance-=amt
    def getbalance(self):
        return self.balance
    def transfer(self,amt,toaccount):
        self.withdraw(amt)
        toaccount.deposit(amt)

print("\t\t\t\tWelcome To Rajdhani Bank\t\t\t\t")
print("\nChoose among our following banking services:")
print("Press 1 to Access your Account")
print("Press 2 to Withdraw Money")
print("Press 3 to Deposit Money")
print("Press 4 to Transfer Money")
print("Press 5 to Create New Account")
print("Press 6 to Enter in testing mode")
ch=int(input ("Enter your choice"))
if ch==6:
    print("\n\nFor testing purposes two Bank Accounts are predefined:")
    print("B1 and B2 with initial balance  10,000 and 5,000 respectively")
    print("Account number (AC/No.) for B1 is 1 And B2 is 2 respectively")
    A=int(input("Enter Your Account Number"))
    if A==1:
        print("Hello Mr.B1")
        B1b=10000
        B1=bankaccount(B1b)
        print("Initial Balance In Account B1=",B1b)
        print ("\nPress 1 To Withdraw Balance")
        print("Press 2 To Deposit Balance")
        chB1=int(input("Enter your choice"))
        if chB1==1:
            X=int(input("Enter the amount to be withdrawn"))
            B1.withdraw(X)
            print(("Balance After Withdrawl="),B1.getbalance())

        elif chB1==2:
            x=int(input ("Enter the amount to be deposited"))
            B1.deposit(x)
            print(("Balance After Deposit="),B1.getbalance())

    elif A==2:
        print("Hello Mr.B2")
        B2b=5000
        B2=bankaccount(B2b)
        print("Initial Balance In Account B2=",B2b)
        chB2=int(input ("Enter your choice"))
        if chB2==1:
             X=int(input("Enter the amount to be withdrawn"))
             B2.withdraw(X)
             print(("Balance After Withdrawl="),B2.getbalance())
        elif chB2==2:
             x=int(input ("Enter the amount to be deposited"))
             B2.deposit(x)
             print(("Balance After Deposit="),B2.getbalance())

    print("\t\t\t\t......Executing Transfer.......\t\t\t\t")

    TB=int(input ("Enter the Amount To Be Transferred"))
    B2.transfer(TB,B1)
    print("Remaining Balance In Account B1=",B1.getbalance())
    print("Remaining Balance In Account B2=",B2.getbalance())
    else:
        print("\t\t\tOOPS!\t\t\t\nYou don't have an account in our bank.")
else:
    print("\nThese functions are under development.\nSorry,for the inconvenience caused")
              
