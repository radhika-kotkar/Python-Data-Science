from functools import reduce

Greater = lambda no : (no >= 70 and no <=90) 
Increment = lambda no : (no + 10)
Product = lambda no1 , no2 : (no1 * no2)

def main():

    Size = 0
    Data = list()
    Size = int(input("Enter the number of Elements :"))

    print("Enter the Elements :")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data is :",Data)

    FData = list(filter(Greater , Data))
    print("Data after Filter :",FData)

    MData = list(map(Increment , FData))
    print("Data after Map :",MData)

    RData = reduce(Product , MData)
    print("Data after Reduce :",RData)

if __name__ == "__main__":
    main()

