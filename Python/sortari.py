import math
import random

def BubbleSort(list):
    for i in range(0,len(list)-1):
        for j in range(0,len(list)-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]


def CountSort(list):
    newList = []
    mini,maxi = min(list),max(list)

    dict = {el:0 for el in range(mini,maxi+1)}
    for el in list:
        dict[el]+=1

    for key in dict.keys():
        newList += [key]*dict[key]

    return newList


def MergeSort(list):
    if len(list) > 1:
        mid = len(list) // 2
        L = list[:mid]
        R = list[mid:]
        MergeSort(L)
        MergeSort(R)

        i = 0
        j = 0
        k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                list[k] = L[i]
                i += 1
                k += 1
            else:
                list[k] = R[j]
                j += 1
                k += 1

        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            list[k] = R[j]
            j += 1
            k += 1


def QuickSort(list, low=0, high=-1):
    if high==-1:
        high = len(list)-1
    if low >= high:
        return list

    index = random.randint(low,high)
    i = low - 1
    for j in range(low, high):
        if list[j] <= list[index]:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i + 1], list[high],index = list[high], list[i+1],i+1

    QuickSort(list, low, index - 1)
    QuickSort(list, index + 1, high)


def mediana(list,a,b,c):
    l3 = [(el,list[el]) for el in [a,b,c]]
    l3.sort(key = lambda t:t[1])
    return l3[1][0]


def QuickSortMedian3(list, low=0, high=-1):
    if high==-1:
        high = len(list)-1
    if low >= high:
        return list

    index = mediana(list,low,high,(low+high)//2)
    i = low - 1
    for j in range(low, high):
        if list[j] <= list[index]:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i + 1], list[high],index = list[high], list[i+1],i+1

    QuickSort(list, low, index - 1)
    QuickSort(list, index + 1, high)


def InsertionSort(list):
    for i in range(1,len(list)):
        index = list[i]
        j = i-1
        while j>=0 and index<list[j]:
            list[j+1] = list[j]
            j = j-1
        list[j+1] = index
    return list


def BucketSort(list):
    nr = int(math.sqrt(len(list)))
    maxi = max(list)
    nr_of_buckets = maxi//nr
    b = [[] for _ in range(0,nr_of_buckets+1)]

    for el in list:
        b[el//nr].append(el)

    for bucket in b:
        InsertionSort(bucket)

    ct = 0
    for bucket in b:
        for el in bucket:
            list[ct] = el
            ct += 1
    return list

def PythonSort(list):
    list.sort()
    return list