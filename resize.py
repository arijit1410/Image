from skimage import io, color, exposure, transform

img=io.imread('a1.jpeg')
img = transform.resize(img, (100,100))
io.imsave('test3.jpeg', img)