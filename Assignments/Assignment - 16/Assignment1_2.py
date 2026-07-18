def ChkNum(no):
    if(no % 2 == 0):
       return True
    else:
        return False

def main():
    value = int(input("Enter the Number :"))

    Ret = ChkNum(value)

    if(Ret == True):
        print("Even Number.")
    else:
        print("Odd Number.")

if __name__ == "__main__":
    main()