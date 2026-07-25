def main():
    try:
        FileName = input("Enter file name : ")
        SearchWord = input("Enter word to search : ")

        fobj = open(FileName, "r")
        print("File gets Opened.")

        Data = fobj.read()

        if SearchWord in Data:
            print("Word is present in the file.")
        else:
            print("Word is not present in the file.")

        fobj.close()

    except FileNotFoundError:
        print("File is not present in Current Directory.")

if __name__ == "__main__":
    main()