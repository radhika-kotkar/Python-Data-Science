import multiprocessing
import os

def EvenSum(No):
    Sum = 0

    for i in range(2, No + 1, 2):
        Sum += i

    print("Process ID :", os.getpid())
    print("Input Number :", No)
    print("Sum of Even Numbers :", Sum)
    print()

    return Sum

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(EvenSum, Data)

    pobj.close()
    pobj.join()

    print(Result)

if __name__ == "__main__":
    main()