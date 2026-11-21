class Account:
    def __init__(self, account_id, owner, balance):
        self.account_id = account_id
        self.owner = owner
        self.balance = balance


    def deposit(self):
        pass


    def withdraw(self):
        pass


    def get_info(self):
        pass


class SavingAccount(Account):
    def __init__(self, account_id, owner, balance, interest_rate):
        super().__init__(account_id, owner, balance)
        self.interest_rate = interest_rate


    def add_interest(self):
        pass


class CheckingAccount(Account):
    def __init__(self, account_id, owner, balance, overdraft_limit):
        super().__init__(account_id, owner, balance)
        self.overdraft_limit = overdraft_limit


    def withdraw(self):
        pass


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
        command = input()

        if command.lower() == "info":
            pass
        elif command.lower() == "deposit":
            pass
        elif command.lower() == "withdraw":
            pass
        elif command.lower() == "interest":
            pass


main()

        