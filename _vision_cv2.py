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