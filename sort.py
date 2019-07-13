def compareLess(leftValue, rightValue):
    return leftValue <= rightValue

def compareMore(leftValue, rightValue):
    return leftValue >= rightValue

def mergeSort(myList, compare):
    if len(myList) <= 1:
        return
    mid = int(len(myList) / 2)
    left = myList[:mid]
    right = myList[mid:]
    mergeSort(left, compare)
    mergeSort(right, compare)
    merge(myList, left, right, compare)


def merge(myList, left, right, compare):
    k = 0
    i = 0
    j = 0
    while ( i < len(left) and  j < len(right)) :
        if (compare(left[i], right[j])):
           myList[k] = left[i]
           i += 1
        else:
            myList[k] = right[j]
            j += 1
        k += 1
    while (i < len(left)):
        myList[k] = left [i]
        i += 1
        k += 1

    while (j < len(right)) :
        myList[k] = right[j]
        j += 1
        k += 1

sortableList1 = [1, 24, 2]
sortableList2 = [32, 21, 12, 99, 8]
mergeSort(sortableList1, compareLess)
print(sortableList1)
mergeSort(sortableList2, compareMore)
print(sortableList2)