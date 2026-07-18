def Rectangle(len,wid):
    Area = len * wid
    return Area 

def main():
    length = int(input("Enter the length of Rectangle :"))
    width = int(input("Enter the width of Rectangle :"))

    Ret = Rectangle(length,width)
    print("Area of Rectangle :",Ret)

if __name__ == "__main__":
    main()