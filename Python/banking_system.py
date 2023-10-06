class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount for deposit. Please enter a positive number.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid amount for withdrawal. Please enter a positive number.")

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: ${self.balance}")


account1 = BankAccount("Isuru Lakmina", 1000)
account2 = BankAccount("John Doe", 500)


account1.check_balance()
account1.deposit(500)
account1.withdraw(200)
account1.check_balance()

account2.check_balance()
account2.deposit(1000)
account2.withdraw(800)
account2.check_balance()
