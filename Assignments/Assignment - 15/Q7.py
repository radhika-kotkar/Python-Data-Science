Greater = lambda large : (len(large) > 5)

def main():
    Size = 0
    Data = list()

    Size = int(input("Enter the Number of Strings :"))
    
    print("Enter the Strings :")

    for i in range(Size):
        val = input()
        Data.append(val)

    print("Input Data is :",Data)

    FData = list(filter(Greater , Data))
    print("Strings having length greater than 5 is :",FData)

if __name__ == "__main__":
    main()