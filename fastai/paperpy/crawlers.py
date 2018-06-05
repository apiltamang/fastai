import os, os.path
import cv2
import numpy as np
from fastai.paperpy.ImageTransform import FormsImageTransform


class FormsCrawler:

    def __init__(self):
        pass

    def crawlPath(self, SRC, DEST):
        images_name = []
        images_clas = []

        for root, dirs, files in os.walk(SRC):
            for f in files:
                fullpath = os.path.join(root, f)
                if f.endswith('.jpg'):

                    splits = fullpath.split("/")
                    mainCls = splits[6].split("_")[0]
                    imgName = splits[-1]

                    if (int(mainCls) == 47):
                        #47 is the class label for white space which I don't want
                        pass
                    else:
                        img = cv2.imread(fullpath)
                        # threshold is used for inverting the image, so that the background appears dark
                        # and the char-pixels appear white and bright
                        threshold = np.max(img) - 45
                        img = FormsImageTransform.processImage(img, np.max(img) - 45)
                        destFile = DEST + "/train/" + imgName
                        cv2.imwrite(destFile, img)
                        images_name.append(imgName)
                        images_clas.append(int(mainCls))

        return images_name, images_clas