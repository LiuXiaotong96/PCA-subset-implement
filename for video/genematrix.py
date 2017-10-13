import numpy as np
from matplotlib import pyplot as plt
import os

def mattoarr(A):
	return A.getA1();

def mataddarr(A,B):
	return np.vstack((A,B))

pathname = './2017'
R=np.zeros((1,2073600))
G=np.zeros((1,2073600))
B=np.zeros((1,2073600))
i=0
filenames = os.listdir(pathname)
filenamenums = []
for filename in filenames:
	filename=filename[:-4]
	filenamenum=long(filename)
	i=i+1
	filenamenums.append(filenamenum)
filenamenums.sort()

for i in range(0,50):
	filename=str(filenamenums[i])
	filename=filename+".bmp"
	filenameta=pathname+"/"+filename
	print filenameta
	original = plt.imread(filenameta)
	R0=np.matrix(original[:,:,0])  
	G0=np.matrix(original[:,:,1])  
	B0=np.matrix(original[:,:,2])
	R=mataddarr(R,mattoarr(R0))
	G=mataddarr(G,mattoarr(G0))
	B=mataddarr(B,mattoarr(B0))
	print i

Rt=R[1:,:].T
Gt=G[1:,:].T
Bt=B[1:,:].T
np.save("R.npy",Rt)
np.save("G.npy",Gt)
np.save("B.npy",Bt)
print "matrix is done"

