def main():
    count = 0

    no = int(input("Enter the Number :"))
    
    while(no != 0):
        count = count + 1
        no = no // 10
    print(count)

if __name__ == "__main__":
    main()