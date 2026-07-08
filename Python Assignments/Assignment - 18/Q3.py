def Minimum(Data):
    Min = Data[0]
    for no in Data:
        if no < Min:
            Min = no
    return Min

def main():
    Size = 0
    Array = list()

    Size = int(input("Enter the Number of Elements :"))

    print("Enter the Elements :")

    for i in range(Size):
        no = int(input())
        Array.append(no)

    Ret = Minimum(Array)
    print(f"Minimum Element is {Ret}.")

if __name__ == "__main__":
    main()

