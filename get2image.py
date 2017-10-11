import numpy as np
from matplotlib import pyplot as plt
import os
from PIL import Image as im

def rebuild(u,s,v,p):
	st=[]
	start=int(len(s)*p)
	for i in range(0,1):
		s[i]=0
	print start
	s=np.diag(s)
	R = np.dot(u.T,s)
	R = np.dot(R,v)
	for array in R:
		array[array<0] = 0
		array[array>255] = 255
	R=np.rint(R).astype("uint8")
	return R
	

Gu=np.load("G2u.npy")
Gv=np.load("G2v.npy")
Gs=np.load("G2s.npy")
Ru=np.load("R2u.npy")
Rv=np.load("R2v.npy")
Rs=np.load("R2s.npy")
Bu=np.load("B2u.npy")
Bv=np.load("B2v.npy")
Bs=np.load("B2s.npy")

G=rebuild(Gu,Gs,Gv,0.1)
G=G.T
i=0
imagesG=np.zeros((230400,))
for image in G:
	imagesG = imagesG+image
	i=i+1

imagesGone=G[0]
imagesG=imagesG/i
imagesG=np.rint(imagesG).astype('uint8')
imagesG=imagesG.reshape((360,640))
imagesGone=np.rint(imagesGone).astype('uint8')
imagesGone=imagesGone.reshape((360,640))
print imagesG
G1=im.fromarray(imagesGone)
Gc=im.fromarray(imagesG)
Gc.save('G2.bmp')

R=rebuild(Ru,Rs,Rv,0.1)
R=R.T
j=0
imagesR=np.zeros((230400,))
for image in R:
	imagesR = imagesR+image
	j=j+1

imagesRone=R[0]
imagesR=imagesR/j
imagesR=np.rint(imagesR).astype('uint8')
imagesR=imagesR.reshape((360,640))
imagesRone=np.rint(imagesRone).astype('uint8')
imagesRone=imagesRone.reshape((360,640))
print imagesR
R1=im.fromarray(imagesRone)
Rc=im.fromarray(imagesR)
Rc.save('R2.bmp')

B=rebuild(Bu,Bs,Bv,0.1)
B=B.T
k=0
imagesB=np.zeros((230400,))
for image in B:
	imagesB = imagesB+image
	k=k+1

imagesBone=B[0]
imagesB=imagesB/k
imagesB=np.rint(imagesB).astype('uint8')
imagesB=imagesB.reshape((360,640))
imagesBone=np.rint(imagesBone).astype('uint8')
imagesBone=imagesBone.reshape((360,640))
print imagesB
B1=im.fromarray(imagesBone)
Bc=im.fromarray(imagesB)
plt.imshow(imagesB, cmap=plt.cm.gray, interpolation='nearest')
Bc.save('B2.bmp')


RGBimage=im.merge('RGB',(Rc,Gc,Bc))
RGBoneimage=im.merge('RGB',(R1,G1,B1))
print RGBimage.mode
RGBimage.show()
RGBimage.save('RGB2.bmp')



































