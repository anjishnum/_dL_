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
      
      
