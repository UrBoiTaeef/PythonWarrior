def getSecondLargest(arr):
    largest = -1
    secondLargest = -1

    for i in arr:
        if i > largest:
            secondLargest = largest
            largest = i
        elif i > secondLargest and i != largest:
            secondLargest = i

    return secondLargest

arr = list(map(int,input("Enter the array elements: ").split()))
result = getSecondLargest(arr)
print(result)