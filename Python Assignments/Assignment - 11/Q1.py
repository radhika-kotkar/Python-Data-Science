# Prime Number : Factors 1 and itself.
# Start from 2 upto val, not to check for all use break and use else for "for loop".

def main():
    val = int(input("Enter the Number :"))

    for i in range(2,val):
        if(val % i == 0):
            print("Not a Prime Number.")
            break
    else:
        print("Prime Number.")

if __name__ == "__main__":
    main()