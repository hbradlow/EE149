from SimpleCV import * 
from ticker import Ticker
import IPython

cam = Camera(0)
t = Ticker()

while True:
    img = cam.getImage()
    img = img.binarize(200).invert()

    blobs = img.findBlobs()
    if blobs:
        for b in blobs:
            img.drawCircle(b.centroid(),10,color=Color.GREEN)
    t.tick()
    img.show()
