# The file which runs by itself named as main.

print("Asking the file it's name?")
print(__name__)     # __main__
print("-" * 40)
# Starter/Dunder - Execution Starts From
# If the file name is main so it will call the main function.

def main():
    print("Main called me!")    
if __name__ == "__main__":
    main()

def main():
    pass    # If we dont want to print anything use pass.
if __name__ == "__main__":
    main()
print("-" * 40)

# def Keyword :

def Display():
    print("Entry Point - Execution starts from Display!")

Display()
Display()
print("End of Application!")
print("-" * 40)

# Addition of two numbers using function :

def main():
    No1 = int(input("Enter the First Number :"))
    No2 = int(input("Enter the second Number"))
    
    Add = No1 + No2
    print("Addition of Number is :",Add)

if __name__ == "__main__":
    main()
print("-" * 40)

# EvenOdd :

def EvenOdd(Val):
    if(Val % 2 == 0):
        print("It's Even Number.")
    else:
        print("It's Odd Number.")

def main():
    No = int(input("Enter the Number :"))

    EvenOdd(No)

if __name__ == "__main__":
    main()
print("-" * 40)
        




