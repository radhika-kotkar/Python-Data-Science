import threading

def EvenList(Data):
    sum = 0

    print("Even Numbers :")
    
    for i in Data:
        if(i % 2 == 0):
            print(i)
            sum = sum + i

    print("Summation of Even Numbers :",sum)

def OddList(Data):
    sum = 0

    print("Odd Numbers :")

    for i in Data:
        if(i % 2 != 0):
            print(i)
            sum = sum + i
            
    print("Summation of Numbers :",sum)

def main():
    Size = 0
    Data = []

    Size = int(input("Enter the Number of Elements :"))

    print("Enter the Elements :")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    t1 = threading.Thread(target = EvenList, args = (Data,))
    t2 = threading.Thread(target = OddList, args = (Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
if __name__ == "__main__":
    main()