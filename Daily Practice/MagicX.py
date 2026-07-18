class Demo:
    def __init__(self,A):
        self.No1 = A

    def __add__(self,other):
        print("Inside __add__")

obj1 = Demo(11)
obj2 = Demo(21)     

print(obj1 + obj2)      # Error - operand error - obj1 and obj2
       