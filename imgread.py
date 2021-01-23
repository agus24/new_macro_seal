from PIL import ImageGrab, Image
import numpy
import cv2
import os

def checkImage(path, th=.8) :
    img_path = os.path.abspath(path)
    pil_img = ImageGrab.grab() #screenshot
    pil_numpy = numpy.array(pil_img, dtype='uint8')\
        .reshape((pil_img.size[1],pil_img.size[0],3))

    screen = pil_numpy

    template = cv2.imread(img_path)
    w, h = template.shape[:-1]

    res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    threshold = th
    loc = numpy.where(res >= threshold)

    print("Image : " + path)
    # print(loc[0])
    # print(loc[1])
    if loc[0].size and loc[1].size :
        return True
    else :
        return False