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

