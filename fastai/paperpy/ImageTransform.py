import cv2
import numpy as np

class ImageTransform:

    def __init__(self):
        self.h, self.w = 28, 28
        self.center = (self.h / 2, self.w / 2)

    def correctImage(self, img):
        ima = cv2.flip(img, 0)
        M = cv2.getRotationMatrix2D(self.center, 270, 1.0)
        ima = cv2.warpAffine(ima, M, (self.w, self.h))
        return ima

class FormsImageTransform:

    def __init__(self):
        pass

    @staticmethod
    def processImage(img, thres):
        tmp = np.copy(img)
        tmp[np.where(tmp > thres)] = 0
        tmp[np.where(tmp != 0)] = 255
        return tmp

if __name__ == "__main__":
    a = ImageTransform()
    print("foobar")