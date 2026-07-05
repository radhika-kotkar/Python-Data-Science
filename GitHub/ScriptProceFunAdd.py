# 1] Scripting Add :

No1 = 11
No2 = 21
Add = No1 + No2 
print("Addition is :",Add)
print("-" * 40)

# 2] Procedural Add :

def Addition(No1,No2):
    return No1 + No2

def main():
    Ret = Addition(10,11)
    print("Addition is :",Ret)

if __name__ == "__main__":
    main()
print("-" * 40)

# 3] Functional Add :

Addition = lambda No1, No2 : No1 + No2

def main():
    Ret = Addition(10,11)
    print("Addition is :",Ret)

if __name__ == "__main__":
    main()
print("-" * 40)

