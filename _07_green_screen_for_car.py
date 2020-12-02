
import matplotlib.image as mpimg #to read the images we want to operate on
import matplotlib.pylab as plt #to plot the images as we move forward
import numpy as np #to operate on images as the erray of numbers
import cv2 #to operate on images for color trasformations and such


#reading the image of the car with green screen in the back
image = mpimg.imread('car_green_screen.jpg')

#printing the dimension of the image
print("Image Dimension: ", image.shape)
#printing the image in the back
plt.imshow(image, cmap='gray')

#color selection limits in terms of saturation of the green color
lowerGreen = np.array([0,180,0])
upperGreen = np.array([100,255,100])

#defining the masked area
mask = cv2.inRange(image,lowerGreen,upperGreen)

#visualize the mask
plt.imshow(mask)

#creating a copy with of main image to be altered
masked_image = np.copy(image)
masked_image [mask != 0] = [0,0,0]

plt.imshow(masked_image)

#loading the image of sky
sky_raw = mpimg.imread('sky.jpg')
#plt.imshow(sky_raw)
#resseting the image size to the firs image to use it later on.
sky = cv2.resize(sky_raw,(660,450))
plt.imshow(sky)


#masked_image [mask!=0] = sky
#plt.imshow(masked_image)

#creating the masked copy for the image of sky
masked_sky = np.copy(sky)
masked_sky [mask == 0] = [0, 0, 0]
plt.imshow(masked_sky)

merged_image = masked_sky+masked_image

plt.imshow(merged_image)

plt.show()