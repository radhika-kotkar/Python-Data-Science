Odd = lambda x : (x % 2 != 0)

def main():
    Size = 0
    Data = list()

    Size = int(input("Enter the Number of Elements :"))
    
    print("Enter the Elements :")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data is :",Data)

    FData = list(filter(Odd , Data))
    print("List of Odd Numbers is :",FData)

if __name__ == "__main__":
    main()