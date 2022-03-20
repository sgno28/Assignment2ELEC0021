from noisyPattern import noisyPattern
import random as rdn
import numpy as np

def createImg():
    image1 = noisyPattern()
    image1.setLines()
    image1.addNoise()

    return image1

def createArray():
    array = np.random.randint(2, size = (3,3))
    array = array * 255
    return array

def main():
    image1 = createImg()
    image1.removeNoise()
    

    #array1 = createArray()
    #array2 = createArray()
    #array3 = createArray()

    #print(array1,"\n")
    #print(array2,"\n")
    #print(array3,"\n")

    #print(findMaj(array1))
    #print(findMaj(array2))
    #print(findMaj(array3))

if __name__ == "__main__":  
    main() 
    