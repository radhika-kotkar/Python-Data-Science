import sys

def CompareFiles(File1, File2):
    try:
        fobj1 = open(File1,"r")
        fobj2 = open(File2,"r")

        Data1 = fobj1.read()
        Data2 = fobj2.read()

        if(Data1 == Data2):
            print("Success")
        else:
            print("Failure")

        fobj1.close()
        fobj2.close()

    except FileNotFoundError:
        print("File is not present in Current Directory.")

def main():

    Border = "-" * 40
    print(Border)
    print("------Marvellous Automation Script------")
    print(Border)

    if(len(sys.argv) == 3):
        CompareFiles(sys.argv[1],sys.argv[2])
    else:
        print("Invalid number of Arguments.")

    print(Border)
    print("ThankYou for using Marvellous Automation Script")
    print(Border)

if __name__ == "__main__":
    main()