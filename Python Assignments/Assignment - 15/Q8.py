Divisible = lambda No : (No % 3 == 0 and No % 5 == 0)

def main():
    Size = 0
    Data = list()

    Size = int(input("Enter the Number of Elements :"))
    
    print("Enter the Elements :")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data is :",Data)

    FData = list(filter(Divisible , Data))
    print("Numbers which are divisible by 3 and 5 is :",FData)

if __name__ == "__main__":
    main()