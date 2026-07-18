import threading

def Small(Str):
    Count = 0

    for ch in Str:
        if ch.islower():
            Count = Count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Small letters :",Count)


def Capital(Str):
    Count = 0

    for ch in Str:
        if ch.isupper():
            Count = Count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Capital letters :",Count)


def Digits(Str):
    Count = 0

    for ch in Str:
        if ch.isdigit():
            Count = Count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Digits :",Count)


def main():

    Str = input("Enter a string : ")

    t1 = threading.Thread(target=Small, args=(Str,), name="Small")
    t2 = threading.Thread(target=Capital, args=(Str,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(Str,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()