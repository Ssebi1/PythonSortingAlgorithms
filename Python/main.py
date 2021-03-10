import sys
sys.setrecursionlimit(10**6)
from sortari import *
from functions import *

sortari = [BubbleSort,CountSort,MergeSort,QuickSort,QuickSortMedian3,BucketSort,InsertionSort,PythonSort]
testcases = ['testcase1.txt','testcase2.txt','testcase3.txt','testcase4.txt','testcase5.txt','testcase6.txt','testcase7.txt','testcase8.txt','testcase9.txt']
g = open('./output.txt', 'w')

for test in testcases:
    print(test)
    g.write(str(test).split('.')[0].capitalize()+':'+'\n')
    list = read_data('./Testcases/'+test)
    for s in sortari:
        time = compute_time(list,s)
        g.write(s.__name__.replace('_',' ') + ': ' + '%.10f'%time+'s'+'\n')
    g.write('\n')

g.close()