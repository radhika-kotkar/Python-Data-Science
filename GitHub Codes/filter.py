# Procedural filter() : EvenOdd

def EvenOdd(No):
    return (No % 2 == 0)

def main():
    Data = [21,17,19,2,24,18]
    print("Input Data is :",Data)

    FData = list(filter(EvenOdd , Data))
    print("Data after Filter :",FData)

if __name__ == "__main__":
    main()
print("-" * 40)

# Functional filter() : EvenOdd

EvenOdd = lambda No : (No % 2 == 0)

def main():
    Data = [21,17,19,2,24,18]
    print("Input Data is :",Data)

    FData = list(filter(EvenOdd , Data))
    print("Data after Filter :",FData)

if __name__ == "__main__":
    main()
print("-" * 40)




