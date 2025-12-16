class BankAccount:
    def init(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Сумма депозита должна быть положительной.")

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Недостаток средств")
        if amount <= 0:
            raise ValueError("Сумма вывода должна быть положительной")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance
