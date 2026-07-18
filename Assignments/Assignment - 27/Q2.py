class BankAccount:
    ROI = 10.5          

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder Name :", self.Name)
        print("Current Balance :", self.Amount)

    def Deposit(self):
        Dep = float(input("Enter amount to deposit : "))
        self.Amount = self.Amount + Dep
        print("Amount Deposited Successfully.")

    def Withdraw(self):
        Wd = float(input("Enter amount to withdraw : "))

        if Wd <= self.Amount:
            self.Amount = self.Amount - Wd
            print("Amount Withdrawn Successfully.")
        else:
            print("Insufficient Balance.")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest

Obj1 = BankAccount("Radhika", 10000)

Obj1.Display()
Obj1.Deposit()
Obj1.Display()
Obj1.Withdraw()
Obj1.Display()
print("Interest :", Obj1.CalculateInterest())

print("-" * 40)

Obj2 = BankAccount("Parth", 5000)

Obj2.Display()
Obj2.Deposit()
Obj2.Withdraw()
Obj2.Display()
print("Interest :", Obj2.CalculateInterest())