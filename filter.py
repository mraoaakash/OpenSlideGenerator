import os
from multiprocessing import Pool
import multiprocessing as mp
import shutil
import numpy as np
import joblib
from Differentiator.hardcode_tester import predict

def filter(path):
    for i in os.listdir(path):
        print(f'Filtering {i}')
        new_path = os.path.join(path, i)
        if not os.path.isdir(os.path.join(new_path, 'rejected')):
            os.makedirs(os.path.join(new_path, 'rejected'))
        rejected = os.path.join(new_path, 'rejected')
        # print(rejected)
        if not os.path.isdir(os.path.join(new_path, 'accepted')):
            os.makedirs(os.path.join(new_path, 'accepted'))
        accepted = os.path.join(new_path, 'accepted')
        # print(accepted)
        model = joblib.load('./Differentiator/finalized_model.sav')
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

def list_creator(path, path_new_level):
    img_list = []
    
    with open(f'{path_new_level}/images.txt', 'w+') as fp:
        for i in os.listdir(path):
            fp.write(f'{i}\n')
        print('Done')
    return



if __name__ == '__main__':
    path = '/storage/bic/data/breastCancer/OpenSlideGenerator/dataset'
    main_path = []
    pool = Pool(mp.cpu_count())
    # for i in os.listdir(path):
    #     main_path.append(os.path.join(path, i))
    
    # pool.map(filter, main_path)
    # pool.close()
    # pool.join()

    # print('Done')

    main_path = []
    path = "/storage/bic/data/breastCancer/OpenSlideGenerator/dataset"    
    for i in os.listdir(path):
        path_new = os.path.join(path, i)
        for j in os.listdir(path_new):
            path_new_level = os.path.join(path_new, j)
            path_new_new = os.path.join(path_new_level, "accepted")
            # print(path_new_new)
            main_path.append(path_new_new)
            print(path_new_level)
            # list_creator(path_new_new, path_new_level)
    print(main_path)