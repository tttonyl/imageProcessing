# why  can not use imshow to show pic?


####### resample ############
from skimage.viewer import ImageViewer as IV
import skimage.io as io
import numpy as np


resample_size = 2 ##### HERE TO CHANGE THE PARAMETER FOR DIFFERENT RESAMPLE SIZE ####
c = io.imread('chronometer.tif')

c_smaller = np.ndarray(shape = (len(range(0,c.shape[0],resample_size)),len(c[1,:][0:c.shape[1]:resample_size])), dtype = "uint8")

for i in range(0,c.shape[0],resample_size):
    c_smaller[i/resample_size,:] = c[i,:][0:c.shape[1]:resample_size]

c_resize = np.ndarray(shape = (c_smaller.shape[0]*resample_size,c_smaller.shape[1]*resample_size), dtype = "uint8")
for i in range(0,c_smaller.shape[0]):
    for j in range(0,c_smaller.shape[1]):
        for h in range(i*resample_size,(i+1)*resample_size):
            for k in range(j*resample_size,(j+1)*resample_size):
                c_resize[h,k] = c_smaller[i,j]

v = IV(c_resize)
v.show()


############ bit plane ############
d = io.imread("dollar.tif")
d_bin = np.ndarray(shape = (500,1192,8))
for i in range(0,d.shape[0]):
    for j in range(0,d.shape[1]):
        for p in range(0,8):
            d_bin[i,j,p] = int('{0:08b}'.format(d[i,j])[::-1][p])*(2**p)
for i in range(8):
    bitmat = IV(d_bin[:,:,i])
    bitmat.show()


######### gray chart ##########


a = np.empty(500)
a[0:100] = 0
a[100:200] = 50
a[200:300] = 100
a[300:400] = 200
a[400:500] = 255
a = a/255.0
b = np.ones(500)
mat = np.outer(a,b)
tt = IV(mat)
tt.show()


'''
gray = io.imread("Gray.jpg")
import matplotlib.pyplot as plt
plt.imshow(gray)
plt.show()
'''
row = np.array([0,12481632...255]).reshape(9,1)

col = np.ones(9).reshape(1,9)
# multiply
grayscale = row * col # 256*256
np.flipip lf

numpy.ndarray.astype(np,uint8) # up,ubyte

gg = np.zero((256,256), dtype = np.ubyte)

gg[:,32:64] = 32
gg[:,64:96] = 32
gg[:,96:128] = 32
gg[:,32:64] = 32
gg[:,32:64] = 32

plt.figure(figsize=(10,10))
plt.axis('off')
plt.imshow(gray,vmax,vmin, cmap=plt.cm.gray,interpolation = 'none')
# %matplotlib
subplot

# parts of figure subplot
subplot(row,col,number of plot)

iage&(~1<<positon)
