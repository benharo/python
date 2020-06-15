import cv2
import numpy as np
# ajustar cámara
cap = cv2.VideoCapture(0)
frames = []
# frame, store in array
while True:
    ret,im = cap.read()
    cv2.imshow('video',im)
    frames.append(im)
    if cv2.waitKey(10) == 27:
        break
    #print(im)
    #print(frames)
frames = np.array(frames)
print(im.shape)
print(frames.shape)