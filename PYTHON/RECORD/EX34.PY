class Bankaccount:
    def __init__(self):
        accountnumber=float(input("enter Account number"))
        nameofholder=str(input("Enter Name of account holder:"))
        typeofaccount=str(input("Enter type of account:"))
        self.balance=0
        
    def deposit(self):
        Amount=float(input("Enter amount to be deposited."))
        self.balance+=Amount
        print("Amount Deposited is", Amount)
    def withdrawl(self):
        Amount=float(input("Enter amount to be withdraw."))
        if self.balance>=Amount:
            self.balance-=Amount
            print("Amount withdrew", Amount)
        else:
            print("Balance is insufficient")
    def display(self):
        print("Available Balance", self.balance)

s=Bankaccount()
s.deposit()
s.withdrawl()
s.display()

# Step 1:start
# Step 2: Create a class bank account
# Step 3:Define a constrctor and three functions display, deposit, withdraw
# Step 4:Create objects
# Step 5:Call the functions and perform the corresponding operations.
# Step 6:stop.