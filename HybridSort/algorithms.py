from turtle import pos


def insertion_sort(data):
    print("Sorting list: ", data)
    for i in range (1, len(data)): #iterate through the list starting from the 2nd element, the elements on the lhs of this index are considered sorted already
        j = i #create a tmp index
        while data[j-1] > data[j] and j > 0: #while the element right to the left of the current element is larger than the current element and the position of the current element is not 0
            data [j-1], data[j] = data[j], data[j-1] #swap the elements value. This means that the current element will enter the LHS of the sorted list and will be slot in position
            j = j - 1 #then decrease the element to go down the sorted list (LHS)
    return data

def bubble_sort(data):
    print("Sorting list: ", data)
    flag = False
    count = 0
    while flag == False:
        flag = True
        for i in range(0, len(data)-1): #in the range of len data - 1 so not including last element. This bubbles up larger elements until the list is in order
            if data[i] > data[i+1]: #if current number is greater than the next number
                flag = False
                data[i], data[i+1] = data[i+1], data[i] #swap the numbers so larger number gets bubbled to the right
        count += 1
    print("count: ", count)
    return data

def selection_sort(data):
    print("Sorting list: ", data)
    for i in range(len(data) - 1):
        smallest = i #set the smallest index to the current element in the remaining list

        for j in range(i+1, len(data)): #iterate through the remaining list after the current element to the end of the list
            if data[j] < data[smallest]: #if the current element is smaller than the initial "smallest" element...
                smallest = j # current element becomes the new smallest
            # this for loop essentially just finds the index posistion of the smallest element

        if smallest != data[i]: #Once index of smallest element is found, if the element in position i is not equal to the element in the index smallest
            data[i], data[smallest] = data[smallest], data[i] #swap the value inside that position 

    return data 

def hybrid_sort(data):
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
    return data
            
def main():
    list0 = [9,2,6,1,4,7,4,8,9,1]
    list1 = [9,2,6,1,4,7,4,8,9,1]
    list2 = [9,2,6,1,4,7,4,8,9,1]
    hybridlist = [9,2,6,1,4,7,4,8,9,1]
    eg = [67, 12, 44, 24, 66]
    print("====================================")
    #print("Insertion sort", insertion_sort(list0))
    #print("====================================")
    #print("bubble: ", bubble_sort(list1))
    #print("====================================")
    #print("selection: ", selection_sort(list2))
    #print("====================================")
    print("Hybrid sort: ", hybrid_sort(eg))

if __name__ == "__main__":
    main()
