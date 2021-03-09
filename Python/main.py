from sortari import *
from functions import *

sortari = [BubbleSort,CountSort,MergeSort,QuickSort,InsertionSort,BucketSort,PythonSort]
testcases = ['testcase1.txt','testcase2.txt','testcase3.txt','testcase4.txt','testcase5.txt']
g = open('./output.txt', 'w')

for test in testcases:
    g.write(str(test).split('.')[0].capitalize()+':'+'\n')
    list = read_data('./Testcases/'+test)
    for s in sortari:
        time = compute_time(list,s)
        g.write(s.__name__.replace('_',' ') + ': ' + '%.10f'%time+'s'+'\n')
    g.write('\n')

g.close()