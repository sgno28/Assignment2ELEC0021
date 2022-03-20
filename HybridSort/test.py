from processArray import processArray as pA

def main():
    array = pA(10)
    print(array.__str__())
    pA.hybridSort(array)

if __name__ == "__main__":
    main()