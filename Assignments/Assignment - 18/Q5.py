import MarvellousNum

def ListPrime(Data):
    Sum = 0

    for No in Data:
        if MarvellousNum.ChkPrime(No):
            Sum = Sum + No

    return Sum

def main():
    Size = int(input("Enter the Number of Elements : "))
    Array = list()

    print("Enter the Elements :")

    for i in range(Size):
        No = int(input())
        Array.append(No)

    Ret = ListPrime(Array)

    print("Addition of Prime Numbers is :", Ret)

if __name__ == "__main__":
    main()