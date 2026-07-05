Square = lambda x : (x * x)

def main():
    Size = 0
    Data = list()

    Size = int(input("Enter the Number of Elements :"))

    print("Enter the Elements :")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data is :",Data)

    MData = list(map(Square , Data))
    print("List of Square of Elements is :",MData)

if __name__ == "__main__":
    main()