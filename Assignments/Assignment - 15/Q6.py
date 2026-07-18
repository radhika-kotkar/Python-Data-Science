from functools import reduce

Minimum = lambda No1 , No2 : No1 if(No1 < No2) else No2

def main():
    Size = 0
    Data = list()

    Size = int(input("Enter the Number of Elements :"))
    
    print("Enter the Elements :")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data is :",Data)

    RData = reduce(Minimum , Data)
    print("Minimum Element is :",RData)

if __name__ == "__main__":
    main()