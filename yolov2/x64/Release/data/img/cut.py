import cv2
import numpy as np

num = 340

for i in range(340,1853):
    try:
    	name = str(i) + ".png"
    	print(name)
    	org_image = cv2.imread(name)
    	img_trim = org_image[65:999, 315:1668]
    	cv2.imwrite(str(i) + ".jpg", img_trim)
    except:
	pass
