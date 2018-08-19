#coding:utf-8
import sys
import os
import getopt


def decrypt(cipherFile, outputFile, keyFile):
    with open(cipherFile, "rb") as cipher:
        chiffre = cipher.read(os.stat(cipherFile).st_size)
        with open(keyFile,"rb") as key:
            cle = key.read(os.stat(keyFile).st_size)
            with open(outputFile, "wb") as out:
                out.write(bytearray([c ^ k for c, k in zip(chiffre, cle)]))
                print("Decrypted")


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:k:o:", ["input", "key", "output"])
    except getopt.GetoptError as e:
        print(e.msg)
        sys.exit(2)
    cipherFile = ""
    keyFile = ""
    outputFile = "output"
    for opt, arg in opts:
        if opt in ("-i", "--input"):
            cipherFile = arg
        elif opt in("-k", "--key"):
            keyFile = arg
        elif opt in ("-o", "--output"):
            outputFile = arg
        else:
            print("Error in arguments")
            sys.exit(2)
    decrypt(cipherFile, outputFile, keyFile)

if __name__ == "__main__":
    main()

