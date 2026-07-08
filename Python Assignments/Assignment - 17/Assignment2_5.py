def main():
    No = int(input("Enter the Number :"))
    
    for i in range(2,No):
        if(No % i == 0):
            print("It is not a Prime Number.")
            break
    else:
        print("It is Prime Number.")
        
if __name__ == "__main__":
    main()
