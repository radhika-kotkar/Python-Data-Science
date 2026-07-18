def Summation(Data):
    Sum = 0
    for no in Data:
        Sum = Sum + no
    return Sum

def main():
    Size = 0
    Array = list()

    Size = int(input("Enter the Number of Elements :"))

    print("Enter the Elements :")

    for i in range(Size):
        no = int(input())
        Array.append(no)

    Ret = Summation(Array)
    print(f"Addition of Elements is {Ret}.")

if __name__ == "__main__":
    main()

