import numpy as np
from matplotlib import pyplot as plt
import os
from PIL import Image as im

def GetR(gray):
	R=np.zeros((405,720))
	for arrays in R:
		for pixel in arrays:
        		if pixel < 127:
            			pixel=0
        		elif pixel > 191:
            			pixel=255
        		else:
            			pixel=(pixel-127)*4-1
	return R


def GetG(gray):
       if gray < 64:
            return 4*gray
       elif gray > 191:
            return 256-(gray-191)*4
       else:
            return 255

def GetB(gray):
        if gray < 64:
            return 255
        elif gray > 127:
            return 0
        else:
            return 256-(gray-63)*4

def Fcolor(image):
	original = plt.imread(image)
	R0=np.matrix(original[:,:,0])  
	G0=np.matrix(original[:,:,1])  
	B0=np.matrix(original[:,:,2])
	R0=(R0*20).getA()
	G0=(G0*20).getA()
	B0=(B0*20).getA()
	R0[R0>255]=255
	G0[G0>255]=255
	B0[B0>255]=255
	R0=np.rint(R0).astype('uint8')
	G0=np.rint(G0).astype('uint8')
	B0=np.rint(B0).astype('uint8')
	R0=im.fromarray(R0)
	G0=im.fromarray(G0)
	B0=im.fromarray(B0)
	RGBimage=im.merge('RGB',(R0,G0,B0))
	RGBimage.show()
	return RGBimage
	

RGBimage = 'RGB2.bmp'
Fcolor(RGBimage)
