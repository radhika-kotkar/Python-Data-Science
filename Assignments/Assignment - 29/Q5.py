def Frequency(FileName, SearchString):
    try:
        fobj = open(FileName,"r")

        Data = fobj.read()

        Count = Data.count(SearchString)

        print("Frequency of",SearchString,"is :",Count)

        fobj.close()

    except FileNotFoundError:
        print("File is not present in Current Directory.")

def main():
    FileName = input("Enter file name : ")
    SearchString = input("Enter string : ")

    Frequency(FileName, SearchString)

if __name__ == "__main__":
    main()