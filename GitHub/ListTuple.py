#-------------------------------------
#   Features        List     Tuple
#-------------------------------------
#   Ordered          Yes     Yes
#   Indexed          Yes     Yes
#   Mutable          Yes     No
#   Heterogeneous    Yes     Yes
#-------------------------------------

# Basic List Program :

def main():
    Data = [10,20,30,40,50]

    print(Data)
    print(type(Data))
    print(len(Data))
    print("-" * 40)

    print(Data[0])
    print(Data[1])
    print(Data[2])
    print(Data[3])
    print(Data[4])
    print("-" * 40)

    Data[2] = 15
    print(Data[2])
    print(Data)
    
if __name__ == "__main__":
    main()
print("-" * 40)


# Basic List Program for Displaying List elements :

def main():
    Marks = [79,84,93,78]
    print("Data from List is :")
    for no in Marks:
        print(no)

if __name__ == "__main__":
    main()
print("-" * 40)

# It will also display the elements.

def main():
    Marks = [79,84,93,78]
    print("Data from List is :")
    for i in range(len(Marks)):
        print(Marks[i])
    
if __name__ == "__main__":
    main()
print("-" * 40)

# Changing the value of List using Index.

def main():
    Marks = [ 78,90,34,97,87]
    for no in Marks:
        print(no)

    Marks[3] = 43

    print("-" * 40)

    for no in Marks:
        print(no)

if __name__ == "__main__":
    main()

# Basic Tuple Program :

def main():
    Data1 = (10,20,30,40,50)

    print(Data1)
    print(type(Data1))
    print(len(Data1))
    print("-" * 40)


    print(Data1[0])
    print(Data1[1])
    print(Data1[2])
    print(Data1[3])
    print(Data1[4])
    
if __name__ == "__main__":
    main()
print("-" * 40)

# Heterogeneous :

def main():
    Data1 = [10, 3.14, True, "Pune"]   
    Data2 = (11, 7.0, False, "Goa")   

    print(Data1)
    print(Data1[0])
    print(Data1[1])
    print(Data1[2])
    print(Data1[3])
    print("-" * 40)
    
    print(Data2)
    print(Data2[0])
    print(Data2[1])
    print(Data2[2])
    print(Data2[3])
    
if __name__ == "__main__":
    main()
print("-" * 40)
