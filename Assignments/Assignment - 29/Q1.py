import os

def CheckFile(FileName):
    Ret = os.path.exists(FileName)

    if(Ret == True):
        print("File is present in Current Directory.")
    else:
        print("There is no such File.")

def main():
    FileName = input("Enter file name : ")

    CheckFile(FileName)

if __name__ == "__main__":
    main()