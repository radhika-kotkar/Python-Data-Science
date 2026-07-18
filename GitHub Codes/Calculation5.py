from CalculationModule import *

def main():
    val1 = int(input("Enter First Number :"))
    val2 = int(input("Enter Second Number :"))

    Ret = Addition(val1 , val2)
    print("Addition is :",Ret)

    Ret = Substraction(val1 , val2)
    print("Substraction is :",Ret)

    Ret = Multiplication(val1 , val2)
    print("Multiplication is :",Ret)

    Ret = Division(val1 , val2)
    print("Division is :",Ret)
    
if __name__ == "__main__":
    main()
print("-" * 40)