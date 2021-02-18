from time import perf_counter

def read_data(file):
    return [int(el) for el in open(file).readline().split()]


def print_data(list):
    print(*list,sep=',')


def compute_time(list,sortingFunction):
    listCopy = list.copy()
    start = perf_counter()
    sortingFunction(listCopy)
    end = perf_counter()
    execution_time = end - start
    return execution_time