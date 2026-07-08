import threading

def CheckPrime(No):
    if No <= 1:
        return False

    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False
    return True

def Prime(Data):
    print("Prime Numbers:")
    for i in Data:
        if CheckPrime(i):
            print(i)

def NonPrime(Data):
    print("Non Prime Numbers:")
    for i in Data:
        if not CheckPrime(i):
            print(i)

def main():

    Size = int(input("Enter number of elements: "))
    Data = []

    print("Enter elements:")
    for i in range(Size):
        Data.append(int(input()))

    t1 = threading.Thread(target=Prime,args=(Data,))
    t2 = threading.Thread(target=NonPrime,args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()