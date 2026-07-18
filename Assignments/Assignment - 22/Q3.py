import multiprocessing
import os

def PrimeCount(No):
    Count = 0

    for i in range(2, No + 1):
        Flag = True

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                Flag = False
                break

        if Flag:
            Count += 1

    print("Process ID :", os.getpid())
    print("Input Number :", No)
    print("Prime Count :", Count)
    print()

    return Count

def main():
    Data = [10000, 20000, 30000, 40000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(PrimeCount, Data)

    pobj.close()
    pobj.join()

    print(Result)

if __name__ == "__main__":
    main()