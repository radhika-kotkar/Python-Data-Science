# Example 1 : Summation of elements

def main():
    Marks = [ 78,90,34,97,87]
    sum = 0
    
    for no in Marks:
        sum = sum + no
    print("Addition is :",sum)

if __name__ == "__main__":
    main()
print("-" * 40)

# Example 2 : Summation using Function call.

def Summation(Data):
    sum = 0
    for no in Data:
        sum = sum + no
    return sum

def main():
    Marks = [ 78,90,34,97,87]

    Ret = Summation(Marks)

    print("Addition is :",Ret)

if __name__ == "__main__":
    main()
print("-" * 40)