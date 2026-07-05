# 1] Accept Values : Nothing    like Ret?
#    Return Values : Nothing    like return Ans?

def Marvellous():
    print("Inside Marvellous")  
    # Only msg is displayed not returned.
def main():
    Marvellous()

if __name__ == "__main__":
    main()
print("-" * 40)

# 2] Accept values : One Parameter
#    Return values : Nothing

def Marvellous(Value):
    print("Inside Marvellous :",Value)

def main():
    Marvellous(11)

if __name__ == "__main__":
    main()
print("-" * 40)

# 3] Accept value : One Parameter
#    Return value : One value

def Marvellous(Value):
    print("Inside Marvellous :",Value)
    return 21

def main():
    Ret = Marvellous(11)
    print("Return value is :",Ret)

if __name__ == "__main__":
    main()
print("-" * 40)

# 4] Accept value : Multiple Parameters
#    Return value : One value

def Marvellous(Val1,Val2):
    print("Inside Marvellous",Val1,Val2)
    return 51

def main():
    Ret = Marvellous(11,21)
    print("Return Value is :",Ret)

if __name__ == "__main__":
    main()
print("-" * 40)

# 5] Accept value : Multiple Parameters
#    Return value : Multiple Values

def Marvellous(Val1,Val2):
    print("Inside Marvellous :",Val1,Val2)
    return 51,101
   
def main():
    Ret1,Ret2 = Marvellous(11,21)
    print("Return Value is :",Ret1,Ret2)

if __name__ == "__main__":
    main()
print("-" * 40)

# Example 1:

def Multiplication(Val1,Val2):
    return Val1 * Val2

def Division(Val1,Val2):
    return Val1 / Val2

def main():
    Ret1 = Multiplication(10,11)
    print("Multiplication is :",Ret1)

    Ret2 = Division(100,10)
    print("Division is :",Ret2)

if __name__ == "__main__":
    main()
print("-" * 40)

# Example 2:

def Calculation(No1,No2):
    Mul = No1 * No2
    Div = No1 / No2
    return Mul,Div

def main():
    Val1 = int(input("Enter the First Number :"))
    Val2 = int(input("Enter the Second Number :"))

    Ret1 , Ret2 = Calculation(Val1,Val2)

    print("Multiplication is :",Ret1)
    print("Division is :",Ret2)

if __name__ == "__main__":
    main()
print("-" * 40)

# Calling the Function which is Inside the Function.

def Prozone():
    print("Hello! I'm inside Prozone Mall.")

    def Zudio():
        print("Heyy! I'm inside Zudio. ")
        
    Zudio()
    # We have to call the fun after the fun is created bcoz interpreter don't get fun before.

def main():
    Prozone()
    
if __name__ == "__main__":
    main()
print("-" * 40)