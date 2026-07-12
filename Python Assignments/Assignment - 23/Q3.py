import multiprocessing
import os

def EvenCount(No):
    Count = 0

    for i in range(2, No + 1, 2):
        Count += 1

    print("Process ID :", os.getpid())
    print("Input Number :", No)
    print("Even Number Count :", Count)
    print()

    return Count

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(EvenCount, Data)

    pobj.close()
    pobj.join()

    print(Result)

if __name__ == "__main__":
    main()