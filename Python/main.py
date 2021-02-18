from sortari import BubbleSort,CountSort,MergeSort
from functions import *

sortari = [BubbleSort,CountSort,MergeSort]
testcases = ['testcase1.txt','testcase2.txt','testcase3.txt']
g = open('./output.txt', 'w')

for test in testcases:
    g.write(str(test).split('.')[0].capitalize()+':'+'\n')
    list = read_data('./Testcases/'+test)
    for s in sortari:
        time = compute_time(list,s)
        g.write(s.__name__ + ': ' + '%.10f'%time+'s'+'\n')
    g.write('\n')