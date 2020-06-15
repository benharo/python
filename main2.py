import matplotlib.pyplot as plt
import optical_flow2

imnames = ['img_1resized.jpg', 'img_2resized.jpg', 'img_3resized.jpg', 'img_4resized.jpg']

# track using the LKTracker generator
lkt = optical_flow2.LKTracker(imnames)
for im,ft in lkt.track():
    print('tracking {} features'.format(len(ft)))
    # plot the tracks
    plt.figure()
    plt.imshow(im)
for p in ft:
    plt.plot(p[0],p[1],'bo')
for t in lkt.tracks:
    plt.plot([p[0] for p in t],[p[1] for p in t])
plt.axis('off')
plt.show()
