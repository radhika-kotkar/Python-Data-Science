def main():
    try:
        FileName = input("Enter file name : ")

        fobj = open(FileName, "r")
        print("File gets Opened.")

        Data = fobj.read()

        Words = Data.split()

        print(f"Total number of words in {FileName} are :", len(Words))

        fobj.close()

    except FileNotFoundError:
        print("File is not present in Current Directory.")

if __name__ == "__main__":
    main()