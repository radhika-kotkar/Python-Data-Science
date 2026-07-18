import multiprocessing
import os

def SumSquare(No):
    Sum = 0

    for i in range(1, No + 1):
        Sum += i * i

    print("Process ID :", os.getpid())
    print("Input Number :", No)
    print("Sum of Squares :", Sum)
    print()

    return Sum

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumSquare, Data)

    pobj.close()
    pobj.join()

    print("Result :", Result)

if __name__ == "__main__":
    main()