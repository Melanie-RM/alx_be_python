import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  
    if len (sys.argv)  < 2:
        print("usage: python main.py <command>:<amount>")
        print(" commands: deposit, withdraw, display")
        sys.exit(1)
    