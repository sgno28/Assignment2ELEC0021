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
        data = self.numbers #set a variable called data which holds the array
        flag = True
        pos = 0 #set position of where the smallest index will be inserted each time (start of remaning list)
        while flag:
            flag = False
            smallest = pos #set the smallest variable initally to the first index of remainig list
            for i in range(pos, len(data) - 1): #iterate through the remaining list
                j = i
                if data[i] > data[i+1]:
                    flag = True
                    data[i], data[i+1] = data[i+1], data[i] #last element will always be the largest

                if data[j] < data[smallest]: #iterating through the data set, find the smallest value
                    smallest = j #store the new index of the smallest value 

            if data[pos] != data[smallest]:
                data[pos], data[smallest] = data[smallest], data[pos] 
                pos += 1 #increse pos for next loop so that next smallest can be slotted in proceeding position

            print("After first iteration while loop: ", data)
