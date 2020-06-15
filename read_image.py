import numpy as np
import cv2

# Cargar imagen a color en grises 0 
# Cargar imagen a color en color 1
img = cv2.imread('robot.jpg',1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()