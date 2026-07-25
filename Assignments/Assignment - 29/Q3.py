import sys

def CopyFile(FileName):
    try:
        fsrc = open(FileName,"r")
        print("Source file gets Opened.")

        fdest = open("Demo.txt","a")
        print("Destination file gets Opened.")

        Data = fsrc.read()

        fdest.write("\n")
        fdest.write(Data)

        print("Contents appended successfully into Demo.txt.")

        fsrc.close()
        fdest.close()

    except FileNotFoundError:
        print("File is not present in Current Directory.")

def main():

    Border = "-" * 40
    print(Border)
    print("------Marvellous Automation Script------")
    print(Border)

    if(len(sys.argv) == 2):
        CopyFile(sys.argv[1])
    else:
        print("Invalid number of Arguments.")

    print(Border)
    print("ThankYou for using Marvellous Automation Script")
    print(Border)

if __name__ == "__main__":
    main()