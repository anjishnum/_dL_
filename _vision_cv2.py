''' Image convolution and compression for feature extraction and blurring effect'''

import cv2
import numpy as np
from scipy import misc
i = misc.ascent()

import matplotlib.pyplot as plt
#plt.grid(False)
#plt.gray()
#plt.axis('off')
#plt.imshow(i)
#plt.show()

i_transformed_1 = np.copy(i)
i_transformed_2 = np.copy(i)
i_transformed_3 = np.copy(i)
size_x = i_transformed_1.shape[0]
size_y = i_transformed_1.shape[1]

filter1 = [ [0, 1, 0], [1, -4, 1], [0, 1, 0]]
filter2 = [ [-1, -2, -1], [0, 0, 0], [1, 2, 1]]
filter3 = [ [-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
weight = 1

for x in range(1,size_x-1):
  for y in range(1,size_y-1):
      convolution = 0.0
      convolution = convolution + (i[x - 1, y-1] * filter1[0][0])
      convolution = convolution + (i[x, y-1] * filter1[0][1])
      convolution = convolution + (i[x + 1, y-1] * filter1[0][2])
      convolution = convolution + (i[x-1, y] * filter1[1][0])
      convolution = convolution + (i[x, y] * filter1[1][1])
      convolution = convolution + (i[x+1, y] * filter1[1][2])
      convolution = convolution + (i[x-1, y+1] * filter1[2][0])
      convolution = convolution + (i[x, y+1] * filter1[2][1])
      convolution = convolution + (i[x+1, y+1] * filter1[2][2])
      convolution = convolution * weight
      if(convolution<0):
        convolution=0
      if(convolution>255):
        convolution=255
      i_transformed_1[x, y] = convolution

for x in range(1,size_x-1):
  for y in range(1,size_y-1):
      convolution = 0.0
      convolution = convolution + (i[x - 1, y-1] * filter2[0][0])
      convolution = convolution + (i[x, y-1] * filter2[0][1])
      convolution = convolution + (i[x + 1, y-1] * filter2[0][2])
      convolution = convolution + (i[x-1, y] * filter2[1][0])
      convolution = convolution + (i[x, y] * filter2[1][1])
      convolution = convolution + (i[x+1, y] * filter2[1][2])
      convolution = convolution + (i[x-1, y+1] * filter2[2][0])
      convolution = convolution + (i[x, y+1] * filter2[2][1])
      convolution = convolution + (i[x+1, y+1] * filter2[2][2])
      convolution = convolution * weight
      if(convolution<0):
        convolution=0
      if(convolution>255):
        convolution=255
      i_transformed_2[x, y] = convolution
      
for x in range(1,size_x-1):
  for y in range(1,size_y-1):
      convolution = 0.0
      convolution = convolution + (i[x - 1, y-1] * filter3[0][0])
      convolution = convolution + (i[x, y-1] * filter3[0][1])
      convolution = convolution + (i[x + 1, y-1] * filter3[0][2])
      convolution = convolution + (i[x-1, y] * filter3[1][0])
      convolution = convolution + (i[x, y] * filter3[1][1])
      convolution = convolution + (i[x+1, y] * filter3[1][2])
      convolution = convolution + (i[x-1, y+1] * filter3[2][0])
      convolution = convolution + (i[x, y+1] * filter3[2][1])
      convolution = convolution + (i[x+1, y+1] * filter3[2][2])
      convolution = convolution * weight
      if(convolution<0):
        convolution=0
      if(convolution>255):
        convolution=255
      i_transformed_3[x, y] = convolution       
      
'''a = []
for x in range(1,size_x-1):
  for y in range(1,size_y-1):
      convolution = 0.0
      convolution = convolution + (i[x - 1, y-1] * filter1[0][0])
      convolution = convolution + (i[x, y-1] * filter1[0][1])
      convolution = convolution + (i[x + 1, y-1] * filter1[0][2])
      convolution = convolution + (i[x-1, y] * filter1[1][0])
      convolution = convolution + (i[x, y] * filter1[1][1])
      convolution = convolution + (i[x+1, y] * filter1[1][2])
      convolution = convolution + (i[x-1, y+1] * filter1[2][0])
      convolution = convolution + (i[x, y+1] * filter1[2][1])
      convolution = convolution + (i[x+1, y+1] * filter1[2][2])
      convolution = convolution * weight
      a.append(convolution)
      if(convolution<0):
        convolution=0
      if(convolution>255):
        convolution=255
      #i_transformed_1[x, y] = convolution
print(min(a))
print(max(a))
print(a.index(max(a)))
print(a.index(min(a)))'''
      
new_x = int(size_x/2)
new_y = int(size_y/2)
newImage_1 = np.zeros((new_x, new_y))
for x in range(0, size_x, 2):
  for y in range(0, size_y, 2):
    pixels = []
    pixels.append(i_transformed_1[x, y])
    pixels.append(i_transformed_1[x+1, y])
    pixels.append(i_transformed_1[x, y+1])
    pixels.append(i_transformed_1[x+1, y+1])
    newImage_1[int(x/2),int(y/2)] = max(pixels)

new_x = int(size_x/2)
new_y = int(size_y/2)
newImage_2 = np.zeros((new_x, new_y))
for x in range(0, size_x, 2):
  for y in range(0, size_y, 2):
    pixels = []
    pixels.append(i_transformed_2[x, y])
    pixels.append(i_transformed_2[x+1, y])
    pixels.append(i_transformed_2[x, y+1])
    pixels.append(i_transformed_2[x+1, y+1])
    newImage_2[int(x/2),int(y/2)] = max(pixels)    
    
new_x = int(size_x/2)
new_y = int(size_y/2)
newImage_3 = np.zeros((new_x, new_y))
for x in range(0, size_x, 2):
  for y in range(0, size_y, 2):
    pixels = []
    pixels.append(i_transformed_3[x, y])
    pixels.append(i_transformed_3[x+1, y])
    pixels.append(i_transformed_3[x, y+1])
    pixels.append(i_transformed_3[x+1, y+1])
    newImage_3[int(x/2),int(y/2)] = max(pixels)    
    
img = [i, i_transformed_1, newImage_1, i, i_transformed_2, newImage_2, i, i_transformed_3, newImage_3]
fig = plt.figure(figsize=(12,12))
for j in range(0,9): 
  fig.add_subplot(3,3,j+1)
  plt.imshow(img[j])
plt.show()
print(filter1)
print(filter2)
print(filter3)    
