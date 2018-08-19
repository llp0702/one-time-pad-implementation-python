#coding:utf-8

import scripts.cryptage as cryptage
import scripts.decryptage as decryptage
import scripts.cryptImg as cryptImg
import scripts.decryptImg as decryptImg
import sys
import getopt


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "cdpi:o:k:", ["crypt", "decrypt", "picture", "input", "output", "key"])
    except getopt.GetoptError as e:
        print(e.msg)
        sys.exit(2)

    decryption = False
    encryption = False
    picture = False
    inputFileName = ""
    outputFileName = ""
    keyFileName = ""

    for opt, arg in opts:
        if opt in ("-c", "--crypt"):
            encryption = True
        elif opt in ("-d", "--decrypt"):
            decryption = True
        elif opt in ("-p", "--picture"):
            picture = True
        elif opt in ("-i", "--input"):
            inputFileName = arg
        elif opt in ("-o", "--output"):
            outputFileName = arg
        elif opt in ("-k", "--key"):
            keyFileName = arg
    if inputFileName == "":
        print(opts)
        print("You must specify an input file")
        sys.exit(2)
    if keyFileName == "" and decryption:
        keyFileName = inputFileName + "key"
    if outputFileName == "":
        outputFileName = "out"
    if picture:
        if encryption:
            cryptImg.cryptImg(inputFileName, outputFileName)
        if decryption:
            if encryption:
                decryptImg.decryptImg(outputFileName, "Decrypt_"+inputFileName, keyFileName)
            else:
                decryptImg.decryptImg(inputFileName, outputFileName, keyFileName)
    else:
        if encryption:
            cryptage.crypt(inputFileName, outputFileName)
        if decryption:
            if encryption:
                decryptage.decrypt(outputFileName, "Decrypt_"+inputFileName, keyFileName)
            else:
                decryptage.decrypt(inputFileName, outputFileName, keyFileName)


if __name__ == "__main__":
    main()
