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
print("Press 5 to create new account")
A=int(input("Enter Your Account Number"))
if A==1:
    print("Hello Mr.B1")
    B1b=int(input("Enter Initial Balance"))
    B1=bankaccount(B1b)
    print("Initial Balance In Account B1=",B1b)
    X=int(input("Enter the amount to be withdrawn"))
    x=int(input ("Enter the amount to be deposited"))
    B1.deposit(x)
    B1.withdraw(X)
    print(("Balance After Deposit="),B1.getbalance())

elif A==2:
    print("Hello Mr.B2")
    B2b=int(input("Enter Initial Balance"))
    B2=bankaccount(B2b)
    print("Initial Balance In Account B2=",B2b)
    X=int(input("Enter the amount to be withdrawn"))
    x=int(input ("Enter the amount to be deposited"))
    B2.deposit(x)
    B2.withdraw(X)
    print(("Balance After Withdrawl="),B2.getbalance())
else:
    print("\t\t\tOOPS!\t\t\t\nYou don't have an account in our bank.")
              
print("\t\t\t\t......Executing Transfer.......\t\t\t\t")

TB=int(input ("Enter the Amount To Be Transferred"))
B2.transfer(TB,B1)
print("Remaining Balance In Account B1=",B1.getbalance())
print("Remaining Balance In Account B2=",B2.getbalance())


        
