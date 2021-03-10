from time import perf_counter
import random

def read_data(file):
    return [int(el) for el in open(file).readline().split()]


def print_data(list):
    print(*list,sep=',')


def compute_time(list,sortingFunction):
    listCopy = list.copy()
    start = perf_counter()
    if len(listCopy) > 10**4:
        if sortingFunction.__name__ == 'BubbleSort' or sortingFunction.__name__ == 'InsertionSort':
            return 0
    if len(listCopy) >= 10**5:
        if sortingFunction.__name__ == 'BucketSort':
            return 0
    sortingFunction(listCopy)
    end = perf_counter()
    print(sortingFunction)
    execution_time = end - start
    return execution_time