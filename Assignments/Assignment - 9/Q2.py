def ChkGreater(Val1,Val2):
    if(Val1 > Val2):
        return True
    else:
        return False
    
def main():
    No1 = int(input("Enter First Number :"))
    No2 = int(input("Enter Second Number :"))

    Ret = ChkGreater(No1 , No2)

    if (Ret == True):
        print(No1,"is Greater.")
    else:
        print(No2,"is Greater.")

if __name__ == "__main__":
    main()