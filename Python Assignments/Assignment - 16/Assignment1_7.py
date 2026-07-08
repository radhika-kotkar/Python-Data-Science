def Divisible(val):
    if(val % 5 ==0):
        return True
    else:
        return False

def main():
    no = int(input("Enter the Number :"))
    Ret = Divisible(no)
    if(Ret == True):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()