from functools import reduce

Product = lambda No1 , No2 : (No1 * No2)

def main():
    Size = 0
    Data = list()

    Size = int(input("Enter the Number of Elements :"))
    
    print("Enter the Elements :")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data is :",Data)

    RData = reduce(Product , Data)
    print("Product of Elements is :",RData)

if __name__ == "__main__":
    main()