import random 
from timeit import default_timer as timer

def mergesort(numbersList):
    arrayLenght = len(numbersList)
    if(arrayLenght <= 1):
        return numbersList
    else:
        middleIndex = arrayLenght//2
        leftList = mergesort(numbersList[:middleIndex])
        rightList = mergesort(numbersList[middleIndex:])
        return merge(leftList, rightList)
        
def merge(left, right):
    sortedArray = []
    while (len(left) > 0 and len(right) != 0):
        if(left[0] > right[0]):
            sortedArray += [right[0]]
            right = right[1:]
        else:
            sortedArray +=[left[0]]
            left = left[1:]
            
    while(len(left) > 0):
        sortedArray += [left[0]]
        left = left[1:]
    
    while(len(right) > 0):
        sortedArray += [right[0]]
        right = right[1:]
    
    return sortedArray

def bubblesort(numbersList):
    arrayLenght = len(numbersList)
    for i in range(arrayLenght):
        swapped = True
        
        for j in range(0, arrayLenght -i - 1):
            if(numbersList[j] > numbersList[j + 1]):
                (numbersList[j],numbersList[j + 1]) = (numbersList[j + 1], numbersList[j])
                swapped = False
        if swapped:
            break                
    return numbersList  

def quickSort(numbersList):
    high = []
    low = []
    pivotList = []

    if(len(numbersList) <= 1):
        return numbersList
    else:
        pivot = numbersList[0]
        for i in numbersList:
            if(i < pivot):
                low += [i]
            elif(i > pivot):
                high += [i]
            else:
                pivotList += [i]
        high = quickSort(high)
        low = quickSort(low)
    return low + pivotList + high

def randomNumbersList(amount, minNumber, maxNumber):
    numbersList = []
    for i in range(amount):
        numbersList += [random.randint(minNumber,maxNumber)]
    return numbersList

def start(amount, minNumber, maxNumber):
    numbersList = randomNumbersList(amount,minNumber,maxNumber)

    startQuickSort = timer()
    quickSort(numbersList)
    endQuickSort = timer()
    print("QuickSort: ",endQuickSort - startQuickSort)

    bubblesort(numbersList)
    endBubbleSort = timer()
    print("BubbleSort: ", endBubbleSort - endQuickSort)

    mergesort(numbersList)
    endMergeSort = timer()
    print("MergeSort: ", endMergeSort- endBubbleSort)
    
def measure(repetitions, amount):
    for i in range(repetitions):
        print("---------------", i, "---------------")
        start(amount, 0, amount)
