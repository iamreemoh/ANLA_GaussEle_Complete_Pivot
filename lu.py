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
    m,n=A.shape
    U=A.copy()                 # U for copy of A
    L=np.identity(m)
    P=np.identity(m)

    Z=np.zeros([m,n])    
    for k in range(m-1):
        imax,jmax= maxabs_idx(U[k:m,k:n])
        # Interchanging Rows
        temp = U[k,:]
        Z[k,:]=U[imax,:].copy()
        Z[imax,:]=temp.copy()
        Z[k+1:imax,:]=U[k+1:imax,:].copy()    # adding between rows as they were
                                    # Z is Partial Pivoted matrix of A

        U=Z.copy()
        for j in range(k+1,m):
            L[j,k]=U[j,k]
            U[j,k:m]=U[j,k:m]-L[j,k]*U[k,k:m]



    return (P, Q, L, U)
