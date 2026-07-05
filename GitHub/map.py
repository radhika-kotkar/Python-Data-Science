# Procedural filter() , map() : EvenOdd , Increment 

def CheckEven(No):
    return (No % 2 == 0)

def Increment(No):
    return No + 1

def main():
    Data = [21,17,19,2,24,18]
    print("Input Data is :",Data)

    FData = list(filter(CheckEven , Data))
    print("Data after Filter :",FData)

    MData = list(map(Increment , FData))
    print("Data after Filter :",MData)

if __name__ == "__main__":
    main()
print("-" * 40)

# Functional filter() , map() : EvenOdd , Increment 

CheckEven = lambda No : (No % 2 == 0)

Increment = lambda No : (No + 1)

def main():
    Data = [21,17,19,2,24,18]
    print("Input Data is :",Data)

    FData = list(filter(CheckEven , Data))
    print("Data after Filter :",FData)

    MData = list(map(Increment , FData))
    print("Data after Filter :",MData)

if __name__ == "__main__":
    main()
print("-" * 40)