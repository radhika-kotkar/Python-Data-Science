# List Input Method 1 :

def main():
    Data = []

    Data.append(11)
    Data.append(21)
    Data.append(51)
    Data.append(101)
    Data.append(111)

    print(Data)

if __name__ == "__main__":
    main()
print("-" * 40)

# List Input Method 2 :

def main():
    Data = []
    print("Enter 5 Elements :")

    no1 = int(input())
    Data.append(no1)
    no2 = int(input())
    Data.append(no2)
    no3 = int(input())
    Data.append(no3)
    no4 = int(input())
    Data.append(no4)
    no5 = int(input())
    Data.append(no5)
    
    print(Data)

if __name__ == "__main__":
    main()
print("-" * 40)

# List Input Method 3 :

def main():
    Data = list()
    print("Enter 5 Elements :")

    no1 = int(input())
    Data.append(no1)
    no2 = int(input())
    Data.append(no2)
    no3 = int(input())
    Data.append(no3)
    no4 = int(input())
    Data.append(no4)
    no5 = int(input())
    Data.append(no5)
    
    print(Data)

if __name__ == "__main__":
    main()
print("-" * 40)

# Dynamic Input Method 1 :

def main():
    Size = 0
    Array = list()

    Size = int(input("Enter the Number of Elements :"))

    print("Enter the Elements :")

    for i in range(Size):
        no = int(input())
        Array.append(no)

    print(Array)

if __name__ == "__main__":
    main()
print("-" * 40)

# Dynamic Input and it's Summation Method 1 :

def Summation(Data):
    Sum = 0
    for no in Data:
        Sum = Sum + no
    return Sum

def main():
    Size = 0
    Array = list()

    Size = int(input("Enter the Number of Elements :"))

    print("Enter the Elements :")

    for i in range(Size):
        no = int(input())
        Array.append(no)

    Ret = Summation(Array)
    print("Addition of Elements is :",Ret)

if __name__ == "__main__":
    main()
print("-" * 40)