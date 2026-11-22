class Account:
    def __init__(self, account_id, owner, balance):
        self.account_id = account_id
        self.owner = owner
        self.balance = balance


    def deposit(self,amount):
        self.balance += amount


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("Insufficient funds")
        return False

        
    def get_info(self):
        return (f"{self.__class__.__name__} | ID: {self.account_id} | Owner: {self.owner} | Balance: {self.balance}")


class SavingAccount(Account):
    def __init__(self, account_id, owner, balance, interest_rate):
        super().__init__(account_id, owner, balance)
        self.interest_rate = interest_rate


    def add_interest(self):
        Profit = self.balance * self.interest_rate / 100
        self.balance += Profit


class CheckingAccount(Account):
    def __init__(self, account_id, owner, balance, overdraft_limit):
        super().__init__(account_id, owner, balance)
        self.overdraft_limit = overdraft_limit


    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            return True
        print("Insufficient funds")
        return False


def main():
    n = int(input())
    accounts = {}
    for _ in range(n):
        type, account_id, owner, balance, extra = input().split()
        account_id = int(account_id)
        balance = int(balance)
        extra = int(extra)
        
        if type.lower() == "savingaccount":
            Acc = SavingAccount(account_id, owner, balance, extra)
        elif type.lower() == "checkingaccount":
            Acc = CheckingAccount(account_id, owner, balance, extra)

        accounts[account_id] = Acc

    q = int(input())
    for _ in range(q):
        command = input().lower()

        if command[0] == "info":
            print(accounts[command[1]].get_info())
        elif command[0] == "deposit":
            accounts[command[1]].deposit(command[2])
        elif command[0] == "withdraw":
            accounts[command[1]].withdraw(command[2])
        elif command[0] == "interest":
            if accounts[command[1]]


main()

        