import numpy as np 

C = [0,0,0,0]
p=0
q=0
r=0
s=0


for i in range(5):
    for i in range(5):
        for i in range(5):
            for i in range(5):
                A = np.array([[9,18,0,0] , [10,21,0,0] , [0,0,9,18] , [0,0,10,21]])
                B = np.array([7+26*p,11+26*q,8+26*r,11+26*s])
                C = np.linalg.solve(A, B)
                print (C)
                p+=1
            q+=1
        r+=1
    s+=1


for i in range(1000):
    A = np.array([[9,18,0,0] , [10,21,0,0] , [0,0,9,18] , [0,0,10,21]])
    B = np.array([7+26*p,11+26*q,8+26*r,11+26*s])
    C = np.linalg.solve(A, B)
    print (C)
    if i<100:
        p+=1
