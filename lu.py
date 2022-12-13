import numpy as np

A= np.array([[1,1,1],[2,3,5],[4,6,8]])

def lu(A):
    # TODO
    U = A.copy()
    m,n = A.shape
    L = np.identity(m)

    for k in range(m-1):
        for j in range(k+1,m):
            L[j,k]=U[j,k]/U[k,k]
            U[j,k:m]= U[j,k:m] - L[j,k]*U[k,k:m]
    return (L, U)

def maxabs_idx(A):
     # TODO
     i,j= np.where(A == A.max())

     return (int(i), int(j))



def lu_complete(A):
    #TODO
    U = None
    L = None
    P = None
    Q = None
    i,j= maxabs_idx(A)
    

    return (P, Q, L, U)
