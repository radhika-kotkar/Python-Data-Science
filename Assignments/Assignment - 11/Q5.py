def main():
    val = int(input("Enter the Number :"))

    rev = 0
    temp = val

    while(val > 0):
        rev = (rev * 10) + ( val % 10)
        val = val // 10         
    
    if(temp == rev):
        print("Palindrome Number.")
    else:
        print("Not a Palindrome Number.")
      
if __name__ == "__main__":
    main()