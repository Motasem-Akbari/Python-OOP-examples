class BankAccount():
    def __init__(self):
        self.__balance = 200000

    def deposit(self, amount):
        self.__balance += amount
        return f"{amount} variz shod ✅ mojodi: {self.__balance}"

    def withdraw(self, amount):
        if self.__balance < amount:
            return f"mojodi kafi nist"
        self.__balance -= amount
        return f"{amount} bardasht shod ✅ mojodi: {self.__balance}"
    
    def get_balance(self):
        return self.__balance

acc = BankAccount()

print(acc.get_balance())
print(acc.deposit(10000))
print(acc.withdraw(110000))