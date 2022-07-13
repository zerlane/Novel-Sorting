def novelSort(arr, left, right):
    if left < right: #base case

        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]

        minIndex, maxIndex = findMinMax(arr, left, right)
        arr[left], arr[minIndex] = arr[minIndex], arr[left]
        arr[right], arr[maxIndex] = arr[maxIndex], arr[right]

        novelSort(arr, left + 1, right - 1)
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

# arr = [8, 5, 2, 13, 11]
# print(novelSort(arr, 0, len(arr) - 1))


#read in file
novelSortFile = open("/Users/zerlane/Documents/UAB Summer22/CS303/Labs/Lab5/NovelSortInput.txt", "r")

inElements = novelSortFile.read()

elementsIntoList = inElements.split("\n\n")

novelSortFile.close()
print(elementsIntoList)
# convert string to time (https://www.educative.io/answers/how-to-convert-a-string-to-a-date-in-python)

#sort method to sort list alphabettically
def alphabetize(arr):
    for i in range (0, len(arr)):
        for j in range(0, len(arr)):
            if(arr[j] > arr[i]):
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
    return arr

print(alphabetize(elementsIntoList))

#bucket sort

def bucketSort (arr, n):
    return arr
