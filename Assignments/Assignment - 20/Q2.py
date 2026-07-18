import threading

def EvenFactor(No):
    sum = 0
    for i in range(1,No+1):
        if(No % i == 0 and i % 2 == 0):
            sum = sum + i
            print(i)

    print("Summation of Even Factors of Number :",sum)

def OddFactor(No):
    sum = 0
    for i in range(1,No+1):
        if(No % i == 0 and i % 2 != 0):
            sum = sum + i
            print(i)
            
    print("Summation of Odd Factors of Number :",sum)

def main():
    Val = int(input("Enter the Number :"))

    t1 = threading.Thread(target = EvenFactor, args = (Val,))
    t2 = threading.Thread(target = OddFactor, args = (Val,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main.")
    
if __name__ == "__main__":
    main()