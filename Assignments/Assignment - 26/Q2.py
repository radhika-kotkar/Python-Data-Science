class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = int(input("Enter the Radius of Circle :"))
        
    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius
        
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius
        
    def Display(self):
        print("Radius is :",self.Radius)
        print("Area is :",self.Area)
        print("Circumference is :",self.Circumference)

cobj1 = Circle()
cobj1.Accept()
cobj1.CalculateArea()
cobj1.CalculateCircumference()
cobj1.Display()

cobj2 = Circle()
cobj2.Accept()
cobj2.CalculateArea()
cobj2.CalculateCircumference()
cobj2.Display()

cobj3 = Circle()
cobj3.Accept()
cobj3.CalculateArea()
cobj3.CalculateCircumference()
cobj3.Display()




        
