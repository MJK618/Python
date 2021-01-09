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
B1=bankaccount(5000)
B2=bankaccount(10000)
print("Initial Balance In Account B1=",5000)
print("Initial Balance In Account B2=",10000)
B1.deposit(1000)
B2.withdraw(1000)
print(("Balance After Deposit="),B1.getbalance())
print(("Balance After Withdrawl="),B2.getbalance())
print("\t\t\t\t......Executing Transfer.......\t\t\t\t")

B2.transfer(500,B1)
print("Remaining Balance In Account B1=",B1.getbalance())
print("Remaining Balance In Account B2=",B2.getbalance())


        
