def BigBazzar():
    print("Inside BigBazzar")

    def Amul():
        print("Inside Amul IceCream Parlour")

def main():
    BigBazzar()          # Allowed
    Amul()               # Error
    BigBazzar.Amul()     # Error
    
if __name__ == "__main__":
    main()