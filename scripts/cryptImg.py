#coding:utf-8
from PIL import Image
import getopt
import os
import sys
import numpy as np


def cryptImg(inputFile, outputFile):
    imageIn = Image.open(inputFile)
    imageOut = imageIn.copy()
    pixelMapIn = imageIn.load()
    pixelMapOut = imageOut.load()
    x = 0
    try:
        sizePixel = len(pixelMapIn[0, 0])
    except TypeError:
        sizePixel = 1
    with open(inputFile + "key", "wb") as keyFile:
        key = os.urandom(sizePixel * imageIn.size[0] * imageIn.size[1])
        keyFile.write(key)
    for i in range(imageIn.size[0]):
        for j in range(imageIn.size[1]):
            try:
                pixelMapOut[i, j] = tuple(np.bitwise_xor(tuple(pixelMapIn[i, j]), tuple(key[x:x + sizePixel])))
            except TypeError :
                pixelMapOut[i,j] = pixelMapIn[i,j] ^ key[x]
            x += sizePixel
    if len(outputFile.split(".")) == 1:
        outputFile += imageIn.format
    imageOut.save(outputFile)
    print("Crypted")
def main():
    try:
        opts,args =getopt.getopt(sys.argv[1:], "i:o:", ["input", "output"])
    except getopt.GetoptError as e:
        print(e.msg)
        sys.exit(2)
    inputFile = ""
    outputFile = "out"
    for opt,arg in opts:
        if opt in ("-i", "--input"):
            inputFile = arg
        elif opt in ("-o", "--output"):
            outputFile = arg
        else :
            print("erreur au niveau des arguments")
    cryptImg(inputFile, outputFile)
if __name__ == "__main__":
    main()

