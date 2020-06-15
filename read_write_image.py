import numpy as np
import cv2

# Cargar imagen a color en grises 0 
# Cargar imagen a color en color 1
img = cv2.imread('robot.jpg',0)
print(img.shape)

cv2.imwrite('robot_g.jpg',img)

cv2.imshow('imagen en gris',img)
cv2.waitKey(0)
cv2.destroyAllWindows()