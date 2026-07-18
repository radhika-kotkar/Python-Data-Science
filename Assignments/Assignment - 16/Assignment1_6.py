def Check(val):
    if(val > 0):
        return True
    elif(val < 0):
        return False
    else:
        return "Zero"

def main():
    no = int(input("Enter the Number :"))
    Ret = Check(no)
    if(Ret == True):
        print("Positive Number.")
    elif(Ret == False):
        print("Negative Number.")
    else:
        print("Zero")

if __name__ == "__main__":
    main()