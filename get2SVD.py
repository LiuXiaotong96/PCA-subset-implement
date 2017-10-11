import numpy as np
from matplotlib import pyplot as plt
import os
import scipy.sparse
from sparsesvd import sparsesvd

R=np.load("R.npy")
R=R.T
R2=np.zeros((1,230400))
print R[2]-R[1]
for i in range(0,364):
	R2=np.vstack((R2,R[i+1]-R[i]))
R2=R2[1:,:].T
print np.shape(R2)
Rcsc = scipy.sparse.csc_matrix(R2)
Ru,Rs,Rv = sparsesvd(Rcsc,100); 
np.save("R2u.npy",Ru)
np.save("R2v.npy",Rv)
np.save("R2s.npy",Rs)

G=np.load("G.npy")
G=G.T
G2=np.zeros((1,230400))
print G[2]-G[1]
for i in range(0,364):
	G2=np.vstack((G2,G[i+1]-G[i]))
G2=G2[1:,:].T
print np.shape(G2)
Gcsc = scipy.sparse.csc_matrix(G2)

Gu,Gs,Gv = sparsesvd(Gcsc,100); 
np.save("G2u.npy",Gu)
np.save("G2v.npy",Gv)
np.save("G2s.npy",Gs)

B=np.load("B.npy")
B=B.T
B2=np.zeros((1,230400))
print B[2]-B[1]
for i in range(0,364):
	B2=np.vstack((B2,B[i+1]-B[i]))
B2=B2[1:,:].T
print np.shape(B2)
Bcsc = scipy.sparse.csc_matrix(B2)
Bu,Bs,Bv = sparsesvd(Bcsc,100); 
np.save("B2u.npy",Bu)
np.save("B2v.npy",Bv)
np.save("B2s.npy",Bs)

