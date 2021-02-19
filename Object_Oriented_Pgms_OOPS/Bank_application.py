class Bank:


    def __init__(self,accno,pname,minbalance):
        self.accountno = accno
        self.personname = pname
        self.balance = minbalance


    def deposit(self,amount):
        self.balance+=amount
        print("acc created with amount ",amount,"suffecient balance",self.balance)

    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print("acc debited with amount ", amount, "suffecient balance", self.balance)



object=Bank(25,"ajay",3000)
object.deposit(5000)
object.withdraw(8000)

