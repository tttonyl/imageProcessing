import numpy
import scipy
import pandas
import matplotlib
from skimage.viewer import ImageViewer as IV
import skimage.io as io
import exifread
from skimage.color import rgb2gray

c = io.imread('/Users/liutongyang/Dropbox/2016GU/imagepro/1/cameraman.tif')
f = io.imread('/Users/liutongyang/Dropbox/2016GU/imagepro/1/flowers-05.tif')

# this command may need a second parameters to control the size of pic?? or put the pic name with quote
io.imshow(c)


viewer = IV(c)
viewer.show()
c.shape
c.ndim
c.size
c.min()
c.max()
c.dtype

viewer = IV(f)
viewer.show()
f.shape
f.ndim
f.size
f.min()
f.max()
f.dtype
# or without saving to a matirx
io.imshow('/Users/liutongyang/Dropbox/2016GU/imagepro/1/flowers-05.tif')

# get info
# ! exiftool xxx.png for other format
f = open("cameraman.tif")
tags = exifread.process_file(f,details = False)
for x in tags:
    print x.ljust(32), ":" , tags[x]



graycmat = rgb2gray(c)
grayc = IV(graycmat)
grayc.show()

graycmat.shape
graycmat.ndim
graycmat.size
graycmat.min()
graycmat.max()
graycmat.dtype




grayfmat = rgb2gray(f)
grayf = IV(grayfmat)
grayf.show()

grayfmat.shape
grayfmat.ndim
grayfmat.size
grayfmat.min()
grayfmat.max()
grayfmat.dtype
