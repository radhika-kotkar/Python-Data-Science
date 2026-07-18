def main():
    Num = int(input("Enter the Number :"))
    
    if(Num % 3 == 0 and Num % 5 == 0):
        print("Number is Divisible by 3 and 5.")
    else:
        print("Number is not Divisible by 3 and 5.")

if __name__ == "__main__":
    main()
