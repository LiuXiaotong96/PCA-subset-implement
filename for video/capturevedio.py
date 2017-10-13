import pylab
import imageio
import skimage
import numpy as np

filename = '1.mp4'
vid = imageio.get_reader(filename,  'ffmpeg')
num=0
for image in vid:
	num=num+1
	print image
	#image = skimage.img_as_float(image).astype(np.float32)
	print type(image)
	imageio.imwrite(str(num)+'.bmp',image)
