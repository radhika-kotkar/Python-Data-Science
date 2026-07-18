# Scripting EvenOdd :

No = 10
if(No % 2 == 0):
    print("It's Even Number.")
else:
    print("It's Odd Number.")
print("-" * 40)

# Procedural EvenOdd :

# def CheckEven(No):
#     return (No % 2 == 0)

def EvenOdd(Val):           
    if(Val % 2 == 0):
        return True
    else:
        return False

def main():
    No = int(input("Enter the Number :"))

    Ret = EvenOdd(No)

    if(Ret == True):
        print("It's Even Number.")
    else:
         print("It's Odd Number.")

if __name__ == "__main__":
    main()
print("-" * 40)
        
# 3] Functional EvenOdd :    

EvenOdd = lambda Val : (Val % 2 == 0)
        
def main():
    No = int(input("Enter the Number :"))

    Ret = EvenOdd(No)       # Ret = (Value % 2 == 0)

    if(Ret == True):
        print("It's Even Number.")
    else:
         print("It's Odd Number.")

if __name__ == "__main__":
    main()
print("-" * 40)

