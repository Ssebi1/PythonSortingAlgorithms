import random

def create_testcase(file,maxi,nr):
    g = open('../Testcases/'+file,'w')
    for _ in range(nr):
        g.write(str(random.randint(0,maxi)) + ' ')
    g.close()


create_testcase('testcase4.txt',10**3,10**3)
create_testcase('testcase5.txt',10**6,10**3)