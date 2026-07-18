import multiprocessing
import os
import time

def SumPower(No):
    Sum = 0

    for i in range(1, No + 1):
        Sum += i ** 5

    print("Process ID :", os.getpid())
    print("Input Number :", No)
    print()

    return Sum

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    Start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumPower, Data)

    pobj.close()
    pobj.join()

    End_time = time.perf_counter()

    print(Result)
    print("Execution Time :", End_time - Start_time)

if __name__ == "__main__":
    main()