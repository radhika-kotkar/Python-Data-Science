EvenCount = lambda No : No % 2 == 0

def main():
    Size = 0
    Data = list()

    Size = int(input("Enter the Number of Elements :"))
    
    print("Enter the Elements :")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data is :",Data)

    FData = len(list(filter(EvenCount , Data)))
    print("Count of Even Numbers is :",FData)

if __name__ == "__main__":
    main()
