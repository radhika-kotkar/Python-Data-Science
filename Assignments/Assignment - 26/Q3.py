class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter the First Number :"))
        self.Value2 = int(input("Enter the Second Number :"))
        
    def Addition(self):
        return self.Value1 + self.Value2
        
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        try:
            return self.Value1 / self.Value2
        except ZeroDivisionError as zobj:
            print("Exception occured due to second operand is zero :",zobj)

Aobj1 = Arithmetic()
Aobj1.Accept()
print("Addition :", Aobj1.Addition())
print("Subtraction :", Aobj1.Subtraction())
print("Multiplication :", Aobj1.Multiplication())
print("Division :", Aobj1.Division())
print("-" * 40)

Aobj2 = Arithmetic()
Aobj2.Accept()
print("Addition :", Aobj2.Addition())
print("Subtraction :", Aobj2.Subtraction())
print("Multiplication :", Aobj2.Multiplication())
print("Division :", Aobj2.Division())
print("-" * 40)


Aobj3 = Arithmetic()
Aobj3.Accept()
print("Addition :", Aobj3.Addition())
print("Subtraction :", Aobj3.Subtraction())
print("Multiplication :", Aobj3.Multiplication())
print("Division :", Aobj3.Division())