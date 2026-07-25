def main():
    try:
        FileName = input("Enter file name : ")

        fobj = open(FileName, "r")
        print("File gets Opened.")

        Lines = fobj.readlines()

        print(f"Total number of lines in {FileName} are :", len(Lines))

        fobj.close()

    except FileNotFoundError:
        print("File is not present in Current Directory.")

if __name__ == "__main__":
    main()