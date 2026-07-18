# Adding the Factors Excluding the Number i.e 12 = (1+2+3+4+6)

def main():
    No = int(input("Enter the Number :"))

    Sum = 0 - No
    
    for i in range(1,No+1):     # range(1,No)
        if(No % i == 0):
            Sum = Sum + i
    print(Sum)
        
if __name__ == "__main__":
    main()
print("-" * 40)  

# Adding the Number too i.2 12 = (1+2+3+4+6+12)

def main():
    No = int(input("Enter the Number :"))

    Sum = 0 
    
    for i in range(1,No+1):
        if(No % i == 0):
            Sum = Sum + i
    print(Sum)
        
if __name__ == "__main__":
    main()
