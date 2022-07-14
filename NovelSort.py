import time

def novelSort(arr, left, right):
    if left < right: #base case

        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]

        minIndex, maxIndex = findMinMax(arr, left, right)
        arr[left], arr[minIndex] = arr[minIndex], arr[left]
        arr[right], arr[maxIndex] = arr[maxIndex], arr[right]

        novelSort(arr, left + 1, right - 1) #takes two from the array
    return arr

def findMinMax(arr, left, right):
    minIndex = left
    maxIndex = left

    for i in range(left + 1, right + 1):
        if arr[i] < arr[minIndex]:
            minIndex = i
        if arr[i] > arr[maxIndex]:
            maxIndex = i

    return minIndex, maxIndex

arr = [8, 5, 2, 13, 11, 43, 36, 24]

print("Array before novel sort algorithm: ")
print(arr)
print("Novel sorting:")
print(novelSort(arr, 0, len(arr) - 1))

print("")

#read in file
novelSortFile = open("/Users/zerlane/Documents/UAB Summer22/CS303/Labs/Lab5/NovelSortInput.txt", "r")
inElements = novelSortFile.read()
elementsIntoList = inElements.split("\n\n")
novelSortFile.close()


#lexicographical sort
def alphabetize(arr): #O(n^2)
    for i in range (0, len(arr)): #n times
        for j in range(0, len(arr)): #n times
            if(arr[j] > arr[i]): #constant time
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
    return arr

print("Alphabetized:")
start = time.time()
alphabetize(elementsIntoList)
end = time.time()

print(f"Execution time: {end - start}")
for i in range(len(elementsIntoList)):
    print(elementsIntoList[i])
