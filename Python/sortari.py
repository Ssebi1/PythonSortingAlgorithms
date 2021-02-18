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
    if len(list)>1:
        mid = len(list) // 2
        L = list[:mid]
        R = list[mid:]
        MergeSort(L)
        MergeSort(R)

        i=0
        j=0
        k=0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                list[k] = L[i]
                i += 1
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