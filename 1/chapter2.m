[w,map] = imread('cameraman.tif');
figure, imshow(w), impixelinfo

size(w)

w(100,200)
impixel(w,100,200)
imfinfo('cameraman.tif')
