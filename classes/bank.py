class Account:
    number = 90192908
    type = "saving account"
    amount = 12,000
    name = "cynthia"
    


class Account:

    def __init__(self,account_name):

       
       
        self.account_name = account_name
        self.balance = 0

    # def check_balance(self):
    #   return f"my account balance is {self.amount}"
    
    def deposit(self,amount):
        self.balance += amount
        return f"you have deposited {amount}you new balance{self.balance}"
    def withdraw(self,amount):
         if self.balance <= amount:
             self.balance -= amount
             return f"you have withdrawn {amount} you new balance is {self.balance}"
         else:
             f"your balance is {self.balance} you can not withdraw {amount}"

#   Add attributes deposits and withdrawals in the init method which are empty lists 
# by default and another attribute loan_balance which is zero by default. 

def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0

account = account_number('123456789', 'John Doe')
# print(account.deposits)      # Output: []
# print(account.withdrawals)   # Output: []
# print(account.loan_balance) 

class BankAccount:

    def __init__(self):
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0

    def deposit(self, amount):
        self.deposits.append(amount)

    def withdraw(self, amount):
        self.withdrawals.append(amount)

    def get_balance(self):
        return sum(self.deposits) - sum(self.withdrawals)

    def get_loan_balance(self):
        return self.loan_balance

    def get_total_balance(self):
        return self.get_balance() + self.get_loan_balance()
    




    class Account:
      category = "Finance"
def __init__(self, account_name):
         self. account_name= account_name=account_name
         self.balance= 0
def deposit(self,amount):
            self.balance += amount
            return f"you have deposited {amount}your new balance is {self.balance}"
def withdraw(self,amount):
            if self.balance<=amount:
               self.balance -=amount
               return f"you have withdrawn{amount} your new balance {self.balance}"
            else: f"your balance s {self.balance} you cannot withdraw{amount}"
            
# Add attributes deposits and withdrawals in the init
# method which are empty lists by default and another
# attribute loan_balance which is zero by default.
def __init__(self, account_name):
        self.account_name = account_name
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0
# Update the withdrawal method to append each withdrawal transaction
# to the withdrawals list. Each transaction should be in form of a
# dictionary like like this
# {
#    "amount": amount,
#    "narration": “withdrawal”
# }
def deposit(self, amount):
        self.balance += amount
        self.deposits.append({
            "amount": amount,
            "narration": "deposit"
        })
        return f"You have deposited {amount}. Your new balance is {self.balance}"
def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.withdrawals.append({
                "amount": amount,
                "narration": "withdrawal"
            })
            return f"You have withdrawn {amount}. Your new balance is {self.balance}"
        else:
            return f"Your balance is {self.balance}. You cannot withdraw {amount}"
# Add a method check_balance which returns the account’s balance
def check_balance(self):
        return f"Your account balance is {self.balance}"
# Add a new method  print_statement which combines both deposits
# and withdrawals into one list and, using a for loop, prints
# each transaction in a new line like this
# deposit - 1000
# withdrawal - 500
def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            print(f"{transaction['narration']} - {transaction['amount']}")
# Add a borrow_loan method which allows a customer to borrow if they meet these conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 1/3 of their total sum of all deposits.
# A successful loan increases the loan_balance by requested amount
def borrow_loan(self, amount):
        if self.loan_balance == 0 and amount > 100 and len(self.deposits) >= 10 and amount <= (sum(
                [transaction['amount'] for transaction in self.deposits]) / 3):
            self.loan_balance += amount
            return f"Loan of {amount} granted. Your loan balance is {self.loan_balance}"
        else:
            return "Loan request denied"
# Add a repay_loan method with this functionality
# A customer can repay a loan to reduce the current loan_balance
# Overpayment of a loan increases the accounts current balance
def repay_loan(self, amount):
        if self.loan_balance > 0:
            if amount > self.loan_balance:
                self.balance += amount - self.loan_balance
                self.loan_balance = 0
                return f"Loan has been fully repaid. Your new balance is {self.balance}"
            else:
                self.loan_balance -= amount
                return f"Loan repayment of {amount} successful. Your loan balance is {self.loan_balance}"
        else:
            return "No outstanding loan"
# Add a transfer method which accepts two attributes
# (amount and instance of another account). If the amount
# is less than the current instances balance, the method
# transfers the requested amount from the current account to
# the passed account. The transfer is accomplished by reducing
# the current account balance and depositing the requested amount
# to the passed account.
def transfer(self, amount, other_account):
        if self.balance >= amount:
            self.balance -= amount
            other_account.deposit(amount)
            return f"Transfer of {amount} to {other_account.account_name} successful."
        else:
            return "Insufficient funds for transfer."
        
    