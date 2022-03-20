from noisyPattern import noisyPattern
import random as rdn
import numpy as np

def createImg():
    image = noisyPattern()
    image.setLines()
    return image

def main():
    #test remove noise
    image1 = createImg()
    image1.addNoise()
    image1.removeNoise()
    
    #test filter1/blur filter
    image2 = createImg()
    image2.filter1()

if __name__ == "__main__":  
    main() 
    