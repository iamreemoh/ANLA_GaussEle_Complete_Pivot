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

    for k in range(m-1):
        imax,jmax= maxabs_idx(U[k:m,k:n])
        print("imax=",imax,"  jmax= ",jmax,"   value= ",U[imax+k,jmax+k])


        # Interchanging Rows
        temp=U[k,:].copy()
        print("iternation ",k+1)
        print(imax,"U[imax] ",U[imax+k,:])
        print("interchanging with ",U[k,:])


        U[k,:]=U[imax+k,:].copy()
        U[imax+k,:]=temp.copy()

        if len(U[k+1:imax,:])!=0:
            U[k+1:imax,:]=U[k+1:imax,:].copy()
        if len(U[imax+1:m+1,:])!=0:
            U[imax+1:m+1,:]=U[imax+1:m+1,:].copy()


        U=U.copy()
    return (P, Q, L, U)