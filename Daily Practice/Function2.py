def Addition(no1 , no2):
    Ans = 0         # Variable inside Function is Local Variable.
    Ans = no1 + no2
    return Ans

def main():
    print("Enter First Number :")
    Value1 = int(input())

    print("Enter Second Number :")
    Value2 = int(input())

    Ret = Addition(Value1 + Value2)

    print("Additon is :",Ret)

if __name__ == "__main__":
    main()
    