# 1] Addition using function call :

def Addition(No1,No2):
    Add = No1 + No2
    return Add

def main():
    val1 = int(input("Enter First Number :"))
    val2 = int(input("Enter Second Number :"))

    Ret = Addition(val1 , val2)
    print("Addition is :",Ret)

if __name__ == "__main__":
    main()
print("-" * 40)