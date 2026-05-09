class BankAccount:
    def __init__(self,account_number,owner_name,balance ):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self,deposit):
        self.balance = self.balance+ deposit
        print(f"you deposited this much amount{deposit}")


    def withdraw(self,withdraw):
        if(withdraw<= self.balance):
           self.balance = self.balance - withdraw
           print(f"you withdraw this much amount {withdraw}")
        else:
            print("insufficient balance")


    def check_balance(self):
        print(f"account owner : {self.owner_name}")
        print(f"current balance is {self.balance}")

account = BankAccount(102,"fatimah",10000)
account.withdraw(5000)
account.check_balance()





