class Demo:
    # Class Variable
    Value = 111

    def __init__(self,A,B):
        # Instance Variables
        self.No1 = A
        self.No2 = B

    # Instance Methods
    def Fun(self):
        print(self.No1)
        print(self.No2)
    
    def Gun(self):
        print(self.No1)
        print(self.No2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.Fun()
obj2.Fun()

obj1.Gun()
obj2.Gun()