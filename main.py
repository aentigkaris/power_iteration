"""
Ntigkaris E. Alexandros
Python v.3.9.2

Power iteration eigenvector & eigenvalue.
"""

import numpy as np

def power_iteration(matrix,vector,N=1000):

    if (np.shape(vector)!=np.shape(matrix) and np.shape(matrix)[0]!=np.shape(matrix)[1]): raise ValueError("Matrix's and vector's shapes not aligned!")

    for i in range(N):
        vector = np.dot(matrix,vector)/np.linalg.norm(matrix*vector)
        eigVal = np.linalg.norm(matrix*vector)
    return vector,eigVal

# input
A = np.array([[4,1,2,1],[1,7,1,0],[2,1,4,1],[1,0,1,3]])
x = np.array([1,2,3,1])

print(f"\nMatrix A:\n{A}\n")
print(f"Randomly-set starting eigenvector:\n{x}\n")

vec,val = power_iteration(A,x)

print(f"eigenvector:\t{vec}\n")
print("eigenvalue:\t%.9f\n"%(val))