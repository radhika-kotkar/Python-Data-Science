Divisible = lambda x : (x % 5 == 0)

def main():
    num = int(input("Enter the Number :"))

    Ret = Divisible(num)

    if(Ret == True):
        print(Ret)
    else:
        print(Ret)
    
if __name__ == "__main__":
    main()   