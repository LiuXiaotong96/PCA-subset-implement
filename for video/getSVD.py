import numpy as np
from matplotlib import pyplot as plt
import os
import scipy.sparse
from sparsesvd import sparsesvd

R=np.load("R.npy")
Rmean=np.mean(R,axis=1)
R=(R.T-Rmean).T
print R
Rcsc = scipy.sparse.csc_matrix(R)
Ru,Rs,Rv = sparsesvd(Rcsc,100); 
np.save("Ru.npy",Ru)
np.save("Rv.npy",Rv)
np.save("Rs.npy",Rs)

G=np.load("G.npy")
Gmean=np.mean(G,axis=1)
G=(G.T-Gmean).T
Gcsc = scipy.sparse.csc_matrix(G)
Gu,Gs,Gv = sparsesvd(Gcsc,100); 
np.save("Gu.npy",Gu)
np.save("Gv.npy",Gv)
np.save("Gs.npy",Gs)

B=np.load("B.npy")
Bmean=np.mean(B,axis=1)
B=(B.T-Bmean).T
Bcsc = scipy.sparse.csc_matrix(B)
Bu,Bs,Bv = sparsesvd(Bcsc,100); 
np.save("Bu.npy",Bu)
np.save("Bv.npy",Bv)
np.save("Bs.npy",Bs)

