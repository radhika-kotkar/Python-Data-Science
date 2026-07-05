# Procedural filter() , map() , reduce() : EvenOdd , Increment , Addition

from functools import reduce

def CheckEven(No):
    return (No % 2 == 0)

def Increment(No):
    return No + 1

def Addition(No1 , No2):
    return No1 + No2

def main():
    Data = [21,17,19,2,24,18]
    print("Input Data is :",Data)

    FData = list(filter(CheckEven , Data))
    print("Data after Filter :",FData)

    MData = list(map(Increment , FData))
    print("Data after Filter :",MData)

    RData = reduce(Addition , MData)    # We dont have to create list again thats why no list() before reduce()
    print("Data after Filter :",RData)
    
if __name__ == "__main__":
    main()
print("-" * 40)

# Functional filter() , map() , reduce() : EvenOdd , Increment , Addition

CheckEven = lambda No : (No % 2 == 0)

Increment = lambda No : (No + 1)

Addition = lambda No1 , No2 : (No1 + No2)

def main():
    Data = [21,17,19,2,24,18]
    print("Input Data is :",Data)

    FData = list(filter(CheckEven , Data))
    print("Data after Filter :",FData)

    MData = list(map(Increment , FData))
    print("Data after Filter :",MData)

    RData = reduce(Addition , MData)    # We dont have to create list again thats why no list() before reduce()
    print("Data after Filter :",RData)

if __name__ == "__main__":
    main()
print("-" * 40)