# Day 17 - OOP: Bank Account Class

# This one defines the class BankAccount
class BankAccount:

    # This is a constructor method which will be automatically called when an instance is created, having params are self, account holders name
    # and balance = 0
    def __init__(self, name, balance = 0):

        # These are the instance variables name and balance with values passed into constructor  
        self.name = name
        self.balance = balance

        # When an account is created this displays the details of that account holder.
        print(f"🏦 Account created for {self.name} with ₹{self.balance} balance.")

    # This method allows the account holder to deposit amount into his / her account. It has two params self and amount to be deposited.
    def deposit(self, amount):

        # If the amount is greater than 0, then only it deposits amount(it won't allows -ve's)
        if amount > 0:

            # Updates / increments the balance by adding amount
            self.balance += amount

            # Displays the msg that amount has deposited
            print(f"💰 {self.name} deposited ₹{amount}. New balance: ₹{self.balance}")

        # If account holder enters -ve amount
        else:
            print("⚠️ Deposit amount must be greater than 0.")

    # # This method allows the account holder to withdraw amount from his / her account. It has two params self and amount to be withdrawn.
    def withdraw(self, amount):

        # The amount will be with drawn if and only if the with drawn amount has to be less than or equal to balance.
        if amount <= self.balance:

            # Then withdraws amount from bank account.
            self.balance -= amount

            # Displays the msg that amount has withdrawn
            print(f"💸 {self.name} withdrew ₹{amount}. Remaining balance: ₹{self.balance}")

        # else alerts the user
        else:
            print("❌ Insufficient funds!")

    # This method allows user to check curent balance in his / her account.
    def check_balance(self):
        print(f"🔎 {self.name}'s current balance: ₹{self.balance}")
        return self.balance

# main:
def main():

    #this one displays a welcome 
    print("🏁 Welcome to Day 17 - Bank Account Class using OOP\n")

    # Create's an account
    user1 = BankAccount("Mahesh babu", 1000)

    # performing operations
    user1.deposit(500)
    user1.withdraw(300)
    user1.check_balance()

    print("\n---\n")

    # Another account
    user2 = BankAccount("Akhil")

    # performing operations 
    user2.deposit(1200)
    user2.withdraw(1500)  # Insufficient
    user2.check_balance()

# # calling main() to starting execution of program
if __name__ == "__main__":
    main()
