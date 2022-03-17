import numpy as np
class processArray:
    def __init__(self,size):
        self.size=2
        self.setSize(size)
        self.numbers=np.random.random([self.size])*100
        self.numbers=self.numbers.round(0)

    def __str__(self):
        return "Array of "+str(self.size)+" numbers"+"\n"+str(self.numbers)

    def setSize(self,size):
        if(size>=2):
            self.size=size

    def hybridSort(self):
    #your code goes here
        pass
