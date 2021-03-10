import random

def create_testcase(file,maxi,nr):
    g = open('../Testcases/'+file,'w')
    for _ in range(nr):
        g.write(str(random.randint(0,maxi)) + ' ')
    g.close()

def create_testcase_equal(file,maxi,nr):
    g = open('../Testcases/'+file,'w')
    n = random.randint(0,maxi)
    for _ in range(nr):
        g.write(str(n) + ' ')
    g.close()

def create_testcase_ascending(file,maxi,nr):
    g = open('../Testcases/'+file,'w')
    for i in range(nr):
        g.write(str(i) + ' ')
    g.close()


create_testcase('testcase3.txt',10**2,10**3)
create_testcase('testcase4.txt',10**3,10**3)
create_testcase('testcase5.txt',10**6,10**3)
create_testcase('testcase6.txt',10**3,10**4)
create_testcase('testcase7.txt',10**6,10**6)
create_testcase_equal('testcase8.txt',10**3,10**3)
create_testcase_ascending('testcase9.txt',10**3,10**3)
