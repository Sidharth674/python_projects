class Account:
    def __init__(self , balance , acc_nu):
        self.balance = balance
        self.acc_nu = acc_nu

    def debit(self , amount):
        self.balance -= amount
        print("RS" , amount , "was debited from your account number" , self.acc_nu)

    def credit(self , amount):
        self.balance += amount
        print("RS" , amount , "was credited to your account number" , self.acc_nu)

    def bal(self):
        print("The total balance in your account having the account number is" , self.balance)

acc1 = Account(1000000 , 12342424245)
print(acc1.balance)
acc1.debit(150000)
print(acc1.balance)
acc1.credit(60000)
print(acc1.balance)