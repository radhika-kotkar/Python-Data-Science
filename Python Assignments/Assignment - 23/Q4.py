import multiprocessing
import os

def OddCount(No):
    Count = 0

    for i in range(1, No + 1, 2):
        Count += 1

    print("Process ID :", os.getpid())
    print("Input Number :", No)
    print("Odd Number Count :", Count)
    print()

    return Count

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(OddCount, Data)

    pobj.close()
    pobj.join()

    print(Result)

if __name__ == "__main__":
    main()