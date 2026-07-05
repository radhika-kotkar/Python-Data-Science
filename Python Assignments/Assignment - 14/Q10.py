Largest = lambda Val1, Val2, Val3 : max(Val1,Val2,Val3)

def main():
    No1 = int(input("Enter the First Number :"))
    No2 = int(input("Enter the Second Number :"))
    No3 = int(input("Enter the Third Number :"))

    Ret = Largest(No1,No2,No3)

    if(No1 >= No2 and No1 >= No3):
        print(No1)
    elif(No2 >= No1 and No2 >= No3):
        print(No2)
    else:
        print(No3)

if __name__ == "__main__":
    main()