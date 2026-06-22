def BigBazzar():    # Outer Function
    print("Inside BigBazzar")

    def Amul():     # Inner/Nested Function(Abstraction)
        print("Inside Amul IceCream Parlour")
    Amul()          # Function Define
    Amul()

def main():
    BigBazzar()          # Allowed
    
if __name__ == "__main__":
    main()