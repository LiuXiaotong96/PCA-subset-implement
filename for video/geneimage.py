import numpy as np
from matplotlib import pyplot as plt
import os
from PIL import Image as im

def rebuild(u,s,v,p):
	st=[]
	start=int(len(s)*p)
	for i in range(0,10):
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
	

Gu=np.load("Gu.npy")
Gv=np.load("Gv.npy")
Gs=np.load("Gs.npy")
Ru=np.load("Ru.npy")
Rv=np.load("Rv.npy")
Rs=np.load("Rs.npy")
Bu=np.load("Bu.npy")
Bv=np.load("Bv.npy")
Bs=np.load("Bs.npy")

G=rebuild(Gu,Gs,Gv,0.02)
G=G.T
i=0
imagesG=np.zeros((2073600,))
for image in G:
	imagesG = imagesG+image
	i=i+1


R=rebuild(Ru,Rs,Rv,0.02)
R=R.T
j=0
imagesR=np.zeros((2073600,))
for image in R:
	imagesR = imagesR+image
	j=j+1


B=rebuild(Bu,Bs,Bv,0.02)
B=B.T
k=0
imagesB=np.zeros((2073600,))
for image in B:
	imagesB = imagesB+image
	k=k+1


for i in range(0,49):

	imagesGone=G[i]
	imagesGone=np.rint(imagesGone).astype('uint8')
	imagesGone=imagesGone.reshape((1920,1080))
	Gc=im.fromarray(imagesGone)

	imagesRone=R[i]
	imagesRone=np.rint(imagesRone).astype('uint8')
	imagesRone=imagesRone.reshape((1920,1080))
	Rc=im.fromarray(imagesRone)

	imagesBone=B[i]
	imagesBone=np.rint(imagesBone).astype('uint8')
	imagesBone=imagesBone.reshape((1920,1080))
	Bc=im.fromarray(imagesBone)

	RGBimage=im.merge('RGB',(Rc,Gc,Bc))
	print RGBimage.mode
	RGBimage.save('./2018/'+str(i)+'.bmp')



































