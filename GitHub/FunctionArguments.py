# Area of Circle : PI*r*r

# 1] Positional Arguments :
 
def Area(Radius,PI):
    Ans = PI * Radius * Radius  
    return Ans

def main():
    Ret = Area(10.5,3.14)
    print("Area of Circle is :",Ret)

    Ret = Area(7.5,12.5)
    print("Area of Circle is :",Ret)

if __name__ == "__main__":
    main()
print("-" * 40)

# 2] Keyword Arguments : Syntax = (Para1 = value , Para2 = value)

def Area(Radius,PI):
    Ans = PI * Radius * Radius
    return Ans

def main():
    Ret = Area(PI = 3.14 , Radius = 6.8)
    print("Area of Circle is :",Ret)

if __name__ == "__main__":
    main()
print("-" * 40)

# 3] Default Arguments : Syntax = (Para1 , Para2 = value)
#                        Error = (Para1 = value , Para2)

def Area(Radius , PI = 3.14):
    Ans = PI * Radius * Radius
    return Ans

def main():
    Ret = Area(10.2)        
    # If 1 value by default it is assigned to Radius.
    print("Area of Circle is :",Ret)

    Ret = Area(5.6 , 8.2)
    print("Area of Circle is :",Ret)

if __name__ == "__main__":
    main()
print("-" * 40)

# 4] Variable Number of Arguments (*args) :
# Datatype is not fixed, all types of data can store and treated as tuple.

def Display(*Data):
    print(Data)
    print(type(Data))

def main():
    Display(10,45.89,False,"Python")
if __name__ == "__main__":
    main()
print("-" * 40)    