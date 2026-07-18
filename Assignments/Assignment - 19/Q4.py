from functools import reduce

Even = lambda no : (no % 2 == 0) 
Square = lambda no : (no ** 2)
Addition = lambda no1 , no2 : (no1 + no2)

def main():

    Size = 0
    Data = list()
    Size = int(input("Enter the number of Elements :"))

    print("Enter the Elements :")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data is :",Data)

    FData = list(filter(Even , Data))
    print("Data after Filter :",FData)

    MData = list(map(Square , FData))
    print("Data after Map :",MData)

    RData = reduce(Addition , MData)
    print("Data after Reduce :",RData)

if __name__ == "__main__":
    main()
