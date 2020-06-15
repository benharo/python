import optical_flow2

imnames = ['img_1resized.jpg', 'img_2resized.jpg', 'img_3resized.jpg', 'img_4resized.jpg']
# create tracker object
lkt = optical_flow2.LKTracker(imnames)
# detect in first frame, track in the remaining
lkt.detect_points()
lkt.draw()
for i in range(len(imnames)-1):
    lkt.track_points()

