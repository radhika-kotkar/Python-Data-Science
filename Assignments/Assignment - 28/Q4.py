def main():
    try:
        SourceFile = input("Enter source file name : ")
        DestinationFile = input("Enter destination file name : ")

        fsrc = open(SourceFile, "r")
        print("Source file gets Opened.")

        fdest = open(DestinationFile, "a")
        print("Destination file gets Opened.")

        Data = fsrc.read()

        fdest.write("\n")
        fdest.write(Data)

        print("Contents copied successfully.")

        fsrc.close()
        fdest.close()

    except FileNotFoundError:
        print("File is not present in Current Directory.")

if __name__ == "__main__":
    main()