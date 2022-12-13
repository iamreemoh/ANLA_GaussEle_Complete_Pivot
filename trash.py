import numpy as np
import numpy as np
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8],[5, 6, 7, 8],[5, 6, 7, 8],[5, 6, 7, 8],[5, 6, 64, 8],[5, 6, 89, 99]])
#print(arr)
#i,j= np.where(arr == arr.max())

def maxabs_idx(A):
     # TODO
     i,j= np.where(A == A.max())

     return (int(i), int(j))

i,j=maxabs_idx(A)
r,c=A.shape
Ac=A.copy()                 # Ac for copy of A

Z=np.zeros([r,c])
# Interchanging Rows
temp = Ac[0,:]
Z[0,:]=Ac[i,:].copy()
Z[i,:]=temp.copy()
Z[1:i,:]=Ac[1:i,:].copy()    # adding between rows as they were
                            # Z is Partial Pivoted matrix of A
ZZ=np.zeros([r,c])
# Interchanging Coloumns
temp_=Z[:, 0]
ZZ[:,0]=Z[:,j].copy()
ZZ[:,j]=temp_.copy()
ZZ[:,1:j]=Z[:,1:j].copy()   # adding between coloumns as they were
print(ZZ)                   # complete Pivoted matrix of A

