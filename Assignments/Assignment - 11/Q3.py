def main():
    val = int(input("Enter the Number :"))

    sum = 0

    while(val > 0):
        rem = val % 10          # To start from last digit i.e remainder.
        sum = sum + rem
        val = val // 10         # To eliminate the number 
    print(sum)
    
if __name__ == "__main__":
    main()