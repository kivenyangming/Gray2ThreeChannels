import cv2
import numpy as np
import os
from tqdm import tqdm


def gray2ThreeChannels(src):
    img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    stacked_img = np.stack((img,) * 3, axis=-1)
    return stacked_img

def Gray2ThreeChannels(RgbImgDir, SaveImgDir):
    img_names = os.listdir(RgbImgDir)
    for img_name in tqdm(img_names):
        if img_name.lower().endswith(
                ('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
            image_path = os.path.join(RgbImgDir, img_name)
            src = cv2.imread(image_path)
            ThreeChannelsImg = gray2ThreeChannels(src)
            if not os.path.exists(SaveImgDir):
                os.makedirs(SaveImgDir)
            SaveImgPath = SaveImgDir + img_name
            cv2.imwrite(SaveImgPath, ThreeChannelsImg)


if __name__ == "__main__":
    RgbImgDir = "./RgbImg/"
    SaveImgDir = "./SaveThreeChannels/"
    Gray2ThreeChannels(RgbImgDir, SaveImgDir)
