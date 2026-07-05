Minimum = lambda Val1 , Val2 : (Val1 < Val2)

def main():
    No1 = int(input("Enter the First Number :"))
    No2 = int(input("Enter the Second Number :"))

    Ret = Minimum(No1,No2)

    if(No1 < No2):
        print(No1)
    else:
        print(No2)

if __name__ == "__main__":
    main()