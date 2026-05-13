
```python
from Account import Account

class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        # Task 1: Added withdraw limit of $100 to the savings account
        self.withdraw_limit = 100

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ${interest:.2f} applied.")

    # Task 2: Overridden withdraw method (amount should not be more than the withdraw limit)
    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print(f"Withdrawal denied: Amount exceeds withdraw limit of ${self.withdraw_limit}")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.get_balance():
            print("Insufficient funds.")
        else:
            super().withdraw(amount)
