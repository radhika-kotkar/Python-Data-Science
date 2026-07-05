import CalculationModule as CM

def main():
    val1 = int(input("Enter First Number :"))
    val2 = int(input("Enter Second Numvber :"))

    Ret = CM.Addition(val1 , val2)

    print("Addition is :",Ret)
    
if __name__ == "__main__":
    main()
print("-" * 40)