def Frequency(Data, No):
    Count = 0

    for i in Data:
        if i == No:
            Count = Count + 1

    return Count

def main():
    Size = int(input("Enter the Number of Elements : "))
    Array = list()

    print("Enter the Elements :")

    for i in range(Size):
        no = int(input())
        Array.append(no)

    Value = int(input("Enter the Number to Search : "))

    Ret = Frequency(Array, Value)

    print("Frequency of", Value, "is :", Ret)

if __name__ == "__main__":
    main()

