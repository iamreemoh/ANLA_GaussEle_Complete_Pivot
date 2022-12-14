import numpy as np
A = np.array([[1,2,3,4,5,6,7,8],
            [9,10,11,12,13,14,15,16],
            [17,18,19,20,21,22,23,24],
            [25,26,27,28,29,30,31,32],
            [33,34,35,36,37,38,39,40],
            [41,42,43,44,45,46,47,48],
            [45,46,47,48,49,50,51,52],
            [53,54,55,56,57,58,59,60]])

def maxabs_idx(A):
    # TODO
    i,j= np.where(A == A.max())
    
    return (int(i),int(j))

m,n=A.shape


def lu_complete(A):
    #TODO
    m,n=A.shape
    U = None
    L=np.identity(m, dtype=np.float32)
    P=np.identity(m)
    Z=np.zeros((m,m),dtype=np.float32)
    Q = np.identity(n)

    _A_=A.copy()                 # _A_ for copy of A
    _A_.astype(np.float32)

    V=A.copy()                 # _A_ for copy of A
    V.astype(np.float32)

    for k in range(m-1):
        imax,jmax= maxabs_idx(_A_[k:m,k:n])
        #imax,jmax= maxabs_idx(V[k:m,k:n])

        #--------------------OOPERATION ON _A_-----------------------------------
        # Interchanging Rows
        temp=_A_[k,:].copy()
        _A_[k,:]=_A_[imax+k,:].copy()
        _A_[imax+k,:]=temp.copy()

        if len(_A_[k+1:imax,:])!=0:
            _A_[k+1:imax,:]=_A_[k+1:imax,:].copy()
        if len(_A_[imax+1:m+1,:])!=0:
            _A_[imax+1:m+1,:]=_A_[imax+1:m+1,:].copy()

        _A_=_A_.copy()
        
        #---------------^^^^^^^----OOPERATION ON _A_-------------^^^^^^^^^------------------

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
        Z[k+1:,k]=np.add(Z[k+1:,k],_A_[k+1:,k])

        #print("iteration ",k,", Z[k+1:,k] =",Z[k+1:,k],"  _A_[k,k]  =",_A_[k,k])
        L[k+1:,k]=np.divide(Z[k+1:,k],_A_[k,k])


        #---------------------------OPERATION ON _A_-----------------------------------------
    #print(_A_)
    #print("\n")
    
    for k in range(m-1):
        imax,jmax= maxabs_idx(_A_[k:m,k:n])

        temp=_A_[:,k].copy()

        _A_[:,k]=_A_[:,jmax+k].copy()
        _A_[:,jmax+k]=temp.copy()

        if len(_A_[:,k+1:jmax])!=0:
            _A_[:,k+1:jmax]=_A_[:,k+1:jmax].copy()
        if len(_A_[:,jmax+1:n+1])!=0:
            _A_[:,jmax+1:n+1]=_A_[:,jmax+1:n+1].copy()

        _A_=_A_.copy()
        #--------------------^^^^^^^--OPERATION ON _A_---^^^^^^^^------------------------------
        #-----------------------------OPERATION ON Q-----------------------------------------

        temp=Q[:,k].copy()

        Q[:,k]=Q[:,jmax+k].copy()
        Q[:,jmax+k]=temp.copy()

        if len(Q[:,k+1:jmax])!=0:
            Q[:,k+1:jmax]=Q[:,k+1:jmax].copy()
        if len(Q[:,jmax+1:n+1])!=0:
            Q[:,jmax+1:n+1]=Q[:,jmax+1:n+1].copy()

    print(L)
    print("\n")
    print(_A_)
    print("\n")
    U=np.multiply(L,_A_)
    print(A)

    return (P, Q, L, U)
lu_complete(A)
