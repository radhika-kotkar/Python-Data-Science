def main():
    try:
        FileName = input("Enter file name : ")

        fobj = open(FileName, "r")
        print("File gets Opened.\n")

        for Line in fobj:
            print(Line, end="")

        fobj.close()

    except FileNotFoundError:
        print("File is not present in Current Directory.")

if __name__ == "__main__":
    main()