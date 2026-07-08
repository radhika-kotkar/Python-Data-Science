def main():
    No = int(input("Enter the Number :"))

    Fact = 1
    
    for i in range(1,No+1):
        Fact = Fact *  i
    print(Fact)
        
if __name__ == "__main__":
    main()