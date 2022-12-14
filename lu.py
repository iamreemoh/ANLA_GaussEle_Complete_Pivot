import numpy as np

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
    i,j= np.unravel_index(A.argmax(), A.shape)
    return (int(i), int(j))


def lu_complete(A):
    #TODO
    m,n=A.shape
    U = np.zeros((m,n))
    L=np.identity(m, dtype=np.float64)
    P=np.identity(m)
    Z=np.zeros((m,m),dtype=np.float64)
    Q = np.identity(n)

    _A_=A.copy()                 # _A_ for copy of A
    _A_.astype(np.float64)

    #-----------------------------For Zero Diagonal element----------------------
    for i in range(m):
        if _A_[i,i]==0:
            if i!=m-1:
                const=_A_[i,:].copy()
                _A_[i,:]=_A_[i+1,:]
                _A_[i+1,:]=const
            else:
                const=_A_[i,:].copy()
                _A_[i,:]=_A_[i-1,:]
                _A_[i-1,:]=const
    #----------------------------------------------------------------------------

    for k in range(m-1):
        imax,jmax= maxabs_idx(_A_[k:m,k:n])

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

        L[k+1:,k]=np.divide(Z[k+1:,k],_A_[k,k])


        #---------------------------OPERATION ON _A_-----------------------------------------
    
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

    
    for i in range(m):
    # iterate through columns of Y
        for j in range(n):
            # iterate through rows of Y
            for k in range(m):
                U[i][j] += L[i][k] * _A_[k][j]

    return (P, Q, L, U)