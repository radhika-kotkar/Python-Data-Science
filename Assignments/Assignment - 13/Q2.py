def Circle(Radius,PI = 3.14):
    Area = PI * Radius * Radius
    return Area

def main():
    rad = int(input("Enter the Radius of Circle :"))

    Ret = Circle(rad)
    print("Area of Circle :",Ret)

if __name__ == "__main__":
    main()