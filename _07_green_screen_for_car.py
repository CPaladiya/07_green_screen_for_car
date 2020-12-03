
import matplotlib.image as mpimg #to read the images we want to operate on
import matplotlib.pylab as plt #to plot the images as we move forward
import numpy as np #to operate on images as the erray of numbers
import cv2 #to operate on images for color trasformations and such

######## --------------- 1.RGB Effect - Creating mask and removing green background from car ------------#########
#reading the image of the car with green screen in the back
image = mpimg.imread('car_green_screen.jpg')

#print("Image Dimension: ", image.shape) #printing the dimension of the image

lowerGreen = np.array([0,180,0]) #color bound for RGB color selection
upperGreen = np.array([100,255,100]) #color bound for RGB color selection

mask = cv2.inRange(image,lowerGreen,upperGreen) #generating the mask for RGB

masked_image = np.copy(image) #creating a copy with of main image to be altered
"""
wherever in mask, the value is not zero (that is representation of green color in original image), 
set 0 in masked image to remove the green color in the masked image
"""
masked_image [mask != 0] = [0,0,0]

plt.imshow(masked_image)


######## --------------- 2.RGB Effect - Adding sky background behind the Car ------------#########

sky_raw = mpimg.imread('sky.jpg') #loading the image of sky

sky = cv2.resize(sky_raw,(660,450)) #resseting the image size to the firs image to use it later on.

masked_sky = np.copy(sky) #creating the masked copy for the image of sky
"""
wherever in mask, the value is zero (that is representation of car in original image), 
set 0 in masked image to set empty space in sky image to fitin the car.
"""
masked_sky [mask == 0] = [0, 0, 0]

#merging the sky with cutout of car and image of car with green background removed
merged_image = masked_sky + masked_image 

plt.imshow(merged_image) #merged image with final output
plt.show()

######## --------------- 3.HSV Effect - Adding sky background behind the Car ------------#########

image2 = mpimg.imread('car_green_screen2.jpg') #loading the image2 car with varying green in the background\

image2_hsv = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV) #converting RGB image to HSV color space

#separating the H,S and V channel form the image
H = image2_hsv[:,:,0]
S = image2_hsv[:,:,1]
V = image2_hsv [:,:,2]

lowerHSV = np.array([50,0,0]) #color bound for RGB color selection
upperHSV = np.array([70,255,255]) #color bound for RGB color selection

mask2 = cv2.inRange(image2_hsv,lowerHSV,upperHSV)
image2_hsv_masked = np.copy(image2)
image2_hsv_masked [mask2 != 0] = [0,0,0]
plt.imshow(image2_hsv_masked)
plt.show()
