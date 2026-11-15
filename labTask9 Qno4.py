class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Amount withdrawn:", amount)

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance:", self.balance)


# Create an object
account1 = BankAccount("Ali", 50000)

# Call methods
account1.deposit(20000)
account1.withdraw(4000)
account1.display_balance()