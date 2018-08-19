#coding:utf-8
import os
import sys
import getopt


def crypt(inputFile, outputFile):
    with open(inputFile, "rb") as inpFile:

        plain = inpFile.read(os.stat(inputFile).st_size)
        key = os.urandom(os.stat(inputFile).st_size)
        print(plain)
        print(key)
        with open(inputFile+"key", "wb") as keyFile:
            keyFile.write(key)
        with open(outputFile, "wb") as outputFile:
            outputFile.write(bytearray([a^b for (a, b) in zip(plain, key)]))
            print("Crypted")


def main():
    try:
        opts,args = getopt.getopt(sys.argv[1:], "i:o:", ["input", "out"])
    except getopt.GetoptError as err:
        print(err.msg)
        sys.exit(2)
    inputFile = ""
    outputFile = "output.otp"
    for opt,arg in opts:
        if opt in ("-i", "--input"):
            inputFile = arg
        elif opt in ("-o", "--out"):
            outputFile = arg
        else:
            print("erreur au niveau des arguments, veuillez executer ce script avec l'option -h afin d'obtenir de l'aide")
    if inputFile == "":
        print("please enter an input file with the option -i {file path}")
        sys.exit(2)
    crypt(inputFile, outputFile)

if __name__ == "__main__":
    main()
