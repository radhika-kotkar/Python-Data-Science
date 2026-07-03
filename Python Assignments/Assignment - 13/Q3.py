def main():
    num = int(input("Enter the Number :"))

    sum = 0

    for i in range(1,num):
        if(num % i == 0):
            sum = sum + i
    if(sum == num):
        print("Perfect Number.")
    else:
        print("Not a Perfect Number.")

if __name__ == "__main__":
    main()