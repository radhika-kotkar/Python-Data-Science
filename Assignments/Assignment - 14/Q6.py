Odd = lambda x : (x % 2 != 0)

def main():
    num = int(input("Enter the Number :"))

    Ret = Odd(num)

    if(Ret == True):
        print(Ret)
    else:
        print(Ret)
    
if __name__ == "__main__":
    main()   