def DisplayFile(FileName):
    try:
        fobj = open(FileName,"r")

        print("File gets Opened.\n")

        Data = fobj.read()

        print(Data)

        fobj.close()

    except FileNotFoundError:
        print("File is not present in Current Directory.")

def main():
    FileName = input("Enter file name : ")

    DisplayFile(FileName)

if __name__ == "__main__":
    main()