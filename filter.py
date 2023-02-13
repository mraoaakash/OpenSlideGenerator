import os
from multiprocessing import Pool
import multiprocessing as mp
import shutil
import numpy as np
import joblib
from Differentiator.hardcode_tester import predict
import warnings
warnings.filterwarnings("ignore")


def predict(path):
    image = Image.open(path)
    image = image.resize((224, 224))
    # print(np.array(image).shape)
    image = np.array(image)
    imageR = image[:,:,0]
    imageG = image[:,:,1]
    imageB = image[:,:,2]
    imageR = imageR.flatten()
    imageG = imageG.flatten()
    imageB = imageB.flatten()
    imageR_mean = np.mean(imageR)
    imageG_mean = np.mean(imageG)
    imageB_mean = np.mean(imageB)
    imageR_std = np.std(imageR)
    imageG_std = np.std(imageG)
    imageB_std = np.std(imageB)
    imageR_sum = np.sum(imageR)
    imageG_sum = np.sum(imageG)
    imageB_sum = np.sum(imageB)
    # print(f'Image Red Channel mean: {imageR_mean}, std: {imageR_std}, sum: {imageR_sum}')
    # print(f'Image Green Channel mean: {imageG_mean}, std: {imageG_std}, sum: {imageG_sum}')
    # print(f'Image Blue Channel mean: {imageB_mean}, std: {imageB_std}, sum: {imageB_sum}')

    total_sum = np.sum(image)
    tota_mean = np.mean(image)
    total_std = np.std(image)
    # print(f'Image total mean: {tota_mean}, std: {total_std}, sum: {total_sum}')
    return (imageR_mean, imageR_std, imageR_sum, imageG_mean, imageG_std, imageG_sum, imageB_mean, imageB_std, imageB_sum, tota_mean, total_std, total_sum,)

masterpath = "/storage/bic/data/breastCancer/OpenSlideGenerator/dataset"
for dirs, subdirs, files in os.walk(masterpath):
    for file in files:
        locpath = os.path.join
    pass