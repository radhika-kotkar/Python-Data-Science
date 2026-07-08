from functools import reduce

Prime = lambda no : no > 1 and all(no%i != 0 for i in range(2,no)) 
Multiply = lambda no : (no * 2)
Maximum = lambda no1 , no2 : no1 if(no1 > no2) else no2

def main():

    Size = 0
    Data = list()
    Size = int(input("Enter the number of Elements :"))

    print("Enter the Elements :")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data is :",Data)

    FData = list(filter(Prime , Data))
    print("Data after Filter :",FData)

    MData = list(map(Multiply , FData))
    print("Data after Map :",MData)

    RData = reduce(Maximum , MData)
    print("Data after Reduce :",RData)

if __name__ == "__main__":
    main()
