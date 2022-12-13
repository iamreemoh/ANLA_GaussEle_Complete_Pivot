import numpy as np
import numpy as np
A = np.array([[10,2,3,4,3,2,5,0],
            [5,6,7,8,4,20,4,4],
            [9,3,2,1,4,1,2,30],
            [5,6,7,8,4,60,4,6],
            [9,3,2,1,4,1,2,80],
            [4,1,3,40,5,6,8,0],
            [5,4,1,3,6,7,6,50],
            [5,6,7,8,4,70,4,0]])

def maxabs_idx(A):
     # TODO
     i,j= np.where(A == A.max())

     return (int(i), int(j))

m,n=A.shape
U=A.copy()
    
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
    
    print("U = ")
    print(U)
    print("\n")
    print("U[k:m,k:n]")
    print(U[k:m,k:n])
