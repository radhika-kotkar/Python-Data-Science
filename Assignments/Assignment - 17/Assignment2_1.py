from Arithmetic import *

def main():
    Val1 = int(input("Enter the First Number :"))
    Val2 = int(input("Enter the Second Number :"))

    Ret = Add(Val1,Val2)
    print(f"Addition is {Ret}")

    Ret = Sub(Val1,Val2)
    print(f"Substraction is {Ret}")

    Ret = Mult(Val1,Val2)
    print(f"Multiplication is {Ret}")

    Ret = Div(Val1,Val2)
    print(f"Division is {Ret}")

if __name__ == "__main__":
    main()
