import cv2
v = [1,2,3]
for i in v:
    src = cv2.imread('img_' + str(i) +'.jpg', cv2.IMREAD_UNCHANGED)
    #percent by which the image is resized
    scale_percent = 50
    #calculate the 50 percent of original dimensions
    print(src.shape)
    width = int(src.shape[1] * scale_percent / 100)
    height = int(src.shape[0] * scale_percent / 100)

    # dsize
    dsize = (width, height)

    # resize image
    output = cv2.resize(src, dsize)

    cv2.imwrite('img_' + str(i) +'resized.jpg',output) 