from venv import create
from noisyPattern import noisyPattern 
import random as rdn
import numpy as np

def createImg():
    image1 = noisyPattern()
    image1.setLines()
    image1.addNoise()

def createArray():
    array = np.random.randint(2, size = (3,3))
    array = array * 255
    return array

def findMaj(A):
    black = 0
    white = 0
    for i in A:
        for j in i:
            if j == 0:
                black +=1
            if j == 255:
                white +=1

    if white > black:
        return ("white", 255)
    if black > white:
        return ("black", 0)

def main():
    createImg()

    array1 = createArray()
    array2 = createArray()
    array3 = createArray()

    print(array1,"\n")
    print(array2,"\n")
    print(array3,"\n")

    print(findMaj(array1))
    print(findMaj(array2))
    print(findMaj(array3))

if __name__ == "__main__":  
    main() 
    