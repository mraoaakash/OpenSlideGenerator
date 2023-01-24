import os
from multiprocessing import Pool
import multiprocessing as mp
import shutil
import numpy as np
import joblib
from Differentiator.hardcode_tester import predict
import warnings
warnings.filterwarnings("ignore")

def filter(path):
    new_path = path
    if not os.path.isdir(os.path.join(new_path, 'rejected')):
        os.makedirs(os.path.join(new_path, 'rejected'))
    rejected = os.path.join(new_path, 'rejected')
    # print(rejected)
    if not os.path.isdir(os.path.join(new_path, 'accepted')):
        os.makedirs(os.path.join(new_path, 'accepted'))
    accepted = os.path.join(new_path, 'accepted')
    # print(accepted)
    model = joblib.load('/storage/bic/data/breastCancer/OpenSlideGenerator/Differentiator/finalized_model.sav')
    # print('Model loaded')
    for image in os.listdir(os.path.join(new_path, 'images')):
        image_path = os.path.join(new_path, 'images', image)
        # print(image_path)
        data = np.array(predict(image_path)).reshape(1, -1)
        prediction = model.predict(data)
        # print(prediction[0])
        if prediction == 'cellSpace':
            # print(f'Accepted {image_path}')
            shutil.copy(image_path, accepted)
        else:
            print (f'Rejected {image_path}')
            shutil.copy(image_path, rejected)
    return

if __name__ == '__main__':
    path = '/storage/bic/data/breastCancer/OpenSlideGenerator/dataset'
    for dirs, subdirs, files in os.walk(path):
        if len(subdirs) == 0:
            print(dirs, subdirs, files, "\n")
    