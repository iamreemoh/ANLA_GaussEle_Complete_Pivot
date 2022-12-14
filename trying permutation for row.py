import numpy as np
A = np.array([[10,2,3,4,3,2,5,0],
            [5,6,7,8,4,20,4,4],
            [9,3,2,1,4,1,2,30],
            [5,6,7,8,4,60,4,6],
            [9,3,2,1,4,1,2,80],
            [4,1,3,40,5,6,8,0],
            [5,5,1,3,6,7,6,50],
            [5,4,7,8,4,70,4,0]])

def maxabs_idx(A):
    # TODO
    i,j= np.where(A == A.max())
    
    return (int(i),int(j))

m,n=A.shape
#print(m,n)
U=A.copy()

def lu_complete(A):
    #TODO
    m,n=A.shape
    U = None
    L=np.identity(m, dtype=np.float32)
    P=np.identity(m)
    Z=np.zeros((m,m),dtype=np.float32)
    Q = None

    U=A.copy()                 # U for copy of A
    U.astype(np.float32)

    V=A.copy()                 # U for copy of A
    V.astype(np.float32)

    for k in range(m-1):
        imax,jmax= maxabs_idx(U[k:m,k:n])
        #imax,jmax= maxabs_idx(V[k:m,k:n])

        #--------------------OOPERATION ON U-----------------------------------
        # Interchanging Rows
        temp=U[k,:].copy()
        U[k,:]=U[imax+k,:].copy()
        U[imax+k,:]=temp.copy()

        if len(U[k+1:imax,:])!=0:
            U[k+1:imax,:]=U[k+1:imax,:].copy()
        if len(U[imax+1:m+1,:])!=0:
            U[imax+1:m+1,:]=U[imax+1:m+1,:].copy()

        U=U.copy()

        temp=V[:,k].copy()

        V[:,k]=V[:,jmax+k].copy()
        V[:,jmax+k]=temp.copy()

        if len(V[:,k+1:jmax])!=0:
            V[:,k+1:jmax]=V[:,k+1:jmax].copy()
        if len(V[:,jmax+1:n+1])!=0:
            V[:,jmax+1:n+1]=V[:,jmax+1:n+1].copy()


        V=V.copy()
        
        #---------------^^^^^^^----OOPERATION ON U-------------^^^^^^^^^------------------

        #------------------------- OPERATION ON P----------------------------------------
        temp=P[k,:].copy()
        P[k,:]=P[imax+k,:].copy()
        P[imax+k,:]=temp.copy()
        if len(P[k+1:imax,:])!=0:
            P[k+1:imax,:]=P[k+1:imax,:].copy()
        if len(P[imax+1:m+1,:])!=0:
            P[imax+1:m+1,:]=P[imax+1:m+1,:].copy()
        
        #----------------^^^^^^--- OPERATION ON P---------------^^^^^^^^^------------------
        
        #------------------------- OPERATION ON L----------------------------------------
        Z[k+1:,k]=np.add(Z[k+1:,k],U[k+1:,k])

        #print("iteration ",k,", Z[k+1:,k] =",Z[k+1:,k],"  U[k,k]  =",U[k,k])
        L[k+1:,k]=np.divide(Z[k+1:,k],U[k,k])


        #---------------^^^^^^----OPERATION ON U------^^^^^^^^^----------------------------
    print(U)
    print("\n")
    
    for k in range(m-1):
        imax,jmax= maxabs_idx(U[k:m,k:n])

        temp=U[:,k].copy()

        U[:,k]=U[:,jmax+k].copy()
        U[:,jmax+k]=temp.copy()

        if len(U[:,k+1:jmax])!=0:
            U[:,k+1:jmax]=U[:,k+1:jmax].copy()
        if len(U[:,jmax+1:n+1])!=0:
            U[:,jmax+1:n+1]=U[:,jmax+1:n+1].copy()


        U=U.copy()
    print(U)

    return (P, Q, L, U)
lu_complete(A)
