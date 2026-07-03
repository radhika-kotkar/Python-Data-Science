def main():
    val = int(input("Enter the Number :"))

    for i in range(1,val+1):
        if(val % i == 0):
            print(i)

if __name__ == "__main__":
    main()