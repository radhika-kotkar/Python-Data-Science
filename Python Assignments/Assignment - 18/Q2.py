def Maximum(Data):
    Max = Data[0]
    for no in Data:
        if no > Max:
            Max = no
    return Max

def main():
    Size = 0
    Array = list()

    Size = int(input("Enter the Number of Elements :"))

    print("Enter the Elements :")

    for i in range(Size):
        no = int(input())
        Array.append(no)

    Ret = Maximum(Array)
    print(f"Maximum Element is {Ret}.")

if __name__ == "__main__":
    main()

