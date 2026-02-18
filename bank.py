class Bank:
    def __init__(self,fname,lname):
        self.__balance = 0
        self.fname = fname
        self.lname = lname
        self.transactions = []

    def deposit(self, amount):
        if amount < 0:
            print("You can't withdraw negative amount")
            return
        self.__balance += amount
        self.transactions.append(f"Deposited {amount}")
        
    def withdraw(self, amount):
        if amount > self.__balance:
            print("You don't have enough money")
            return
        if amount < 0:
            print("You can't withdraw negative amount")
            return
        if amount == 0:
            print("You can't withdraw 0 amount")
            return
        self.__balance -= amount
        self.transactions.append(f"Withdrew {amount}")
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        self.__balance = amount
        
    def show_transactions(self):
        for transaction in self.transactions:
            print(transaction)
        
if __name__ == "__main__":
    bank = Bank("John", "Doe")
    bank.deposit(100)
    bank.withdraw(50)
    bank.show_transactions()