#coding:utf-8
from PIL import Image
import sys
import numpy as np
import getopt


def decryptImg(inputFileName, outputFileName, keyFileName) :
    with open(keyFileName, "rb") as keyFile:
        imageIn = Image.open(inputFileName)
        imageOut = imageIn.copy()
        pixelMapIn = imageIn.load()
        pixelMapOut = imageOut.load()
        try:
            pixelSize = len(pixelMapIn[0, 0])
        except TypeError:
            pixelSize = 1
        for i in range(imageOut.size[0]):
            for j in range(imageOut.size[1]):
                key = keyFile.read(pixelSize)
                try:
                    pixelMapOut[i, j] = tuple(np.bitwise_xor(pixelMapIn[i, j], tuple(key)))
                except TypeError:
                    pixelMapOut[i, j] = pixelMapIn[i, j] ^ key
        if len(outputFileName.split(".")) == 1:
            outputFileName += imageIn.format
        imageOut.save(outputFileName)
        print("Decrypted")


def main():
    try:
        opts,args = getopt.getopt(sys.argv[1:], "k:i:o:", ["key", "input", "output"])
    except getopt.GetoptError as e:
        print(e.msg)
        sys.exit(2)
    keyFileName = ""
    inputFileName = ""
    outputFileName = "out"
    for opt,arg in opts:
        if opt in ("-k", "--key") :
            keyFileName = arg
        elif opt in ("-i", "--input"):
            inputFileName = arg
        elif opt in ("-o", "--output"):
            outputFileName = arg
        else:
            print("erreur au niveau des arguments")
            sys.exit(2)
    decryptImg(inputFileName, outputFileName, keyFileName)
if __name__ == "__main__":
    main()
