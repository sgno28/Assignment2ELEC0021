from cmath import pi
from re import L
import numpy as np
import random
import matplotlib.pyplot as plt

class noisyPattern:
    def __init__(self):
        self.image=np.full([80,80],255)
        self.setLines()
 
    def setLines(self):
        self.image[:,0:16]=0 #sets ALL y elements in x positions 0->16 = 0
        self.image[:,32:48]=0
        self.image[:,64:80]=0
        plt.imsave('lines.png', self.image, cmap=plt.cm.gray)
    
    def addNoise(self):
        noise=0.05
        for i in range (0,self.image.shape[0]):
            for j in range(0,self.image.shape[1]):
                if(noise > random.random()):
                    self.image[i,j]=255 
        plt.imsave('noisy_pattern.png', self.image, cmap=plt.cm.gray)
    
    def __getMajority(self, i, j):
        temp_array = self.image[i-1:i+2, j-1:j+2] #create temporary array of the surrounding pixels
        sum = temp_array.sum() - 255 #sums every element in the array and minus the middle pixel
        maj = sum / 8 #gets majority sum of pixels
        if maj < 127.5: #255/2, if below this threshold then majority is black
            return 0
        else:
            return 255


    def removeNoise(self):
        noise_removed = np.copy(self.image) #make object copy of original image with noise so that I can work on the original image without changing it as I go

        rows = self.image.shape[0]
        cols = self.image.shape[1]

        whitePixels = np.where(self.image == 255) #find the indexes of all instances of white pixels in noisy image
        wp_coords = list(zip(whitePixels[0], whitePixels[1])) #zip the two arrays together to get their indexs in coords format

        for pixels in wp_coords:
            if pixels[0] != 0 and pixels[0] != (rows - 1) and pixels[1] !=0 and pixels[1] != (cols - 1): #if these arnt the pixels on the borders
                i, j = pixels[0], pixels[1] #assign the coordinates of that pixel to a i and j system
                maj = self.__getMajority(i, j)
                if maj == 0:
                    noise_removed[i, j] = 0 #if majority is black then change the pixel to black 

        self.image = noise_removed #reassign the image to the final noise removed image
        plt.imsave("noise_removed.png", self.image, cmap = plt.cm.gray) #plot new image

    def filter1(self):
        #your code here
        #replace the value of every pixel by the average of the values
        #of its neighbouring pixels
        #save the resulting image in file pattern_filter1.pn
        pass