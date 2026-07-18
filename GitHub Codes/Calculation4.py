from CalculationModule import Addition, Substraction

def main():
    val1 = int(input("Enter First Number :"))
    val2 = int(input("Enter Second Numvber :"))

    Ret = Addition(val1 , val2)
    print("Addition is :",Ret)

    Ret = Substraction(val1 , val2)
    print("Substraction is :",Ret)
    
if __name__ == "__main__":
    main()
print("-" * 40)