def main():
    val = int(input("Enter the Number :"))

    rev = 0

    while(val > 0):
        rev = (rev * 10) + ( val % 10)
        val = val // 10         
    print(rev)
      
if __name__ == "__main__":
    main()