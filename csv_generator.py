import os
from multiprocessing import Pool
import multiprocessing as mp
import openslide
from openslide.deepzoom import DeepZoomGenerator
from PIL import Image
import numpy as np


def list_creator(path):
    for dirs, subdirs, files in os.walk(path):
        for file in files:
            if file.endswith('.tif'):
                if "HNE" in file.upper():
                    print(file)
                    try:
                        tile_size = 256
                        image = openslide.OpenSlide(os.path.join(dirs, file))
                        # print(image.dimensions)
                        dzoomImg = DeepZoomGenerator(image, tile_size=tile_size, overlap=0, limit_bounds=True)
                        print(dzoomImg.level_count)
                        print(dzoomImg.level_tiles)
                        print(dzoomImg.level_dimensions)
                        for i in range(9,dzoomImg.level_count):    
                            # deepzwsi = dzoomImg.get_tile(i, address = (0, 0))
                            # print(deepzwsi)
                            leveltiles = dzoomImg.level_tiles[i]
                            print(f'leveltiles_{i} : {leveltiles}')
                            for j in range(0,leveltiles[0]):
                                for k in range(0,leveltiles[1]):
                                    deepzwsi = dzoomImg.get_tile(i, address = (j, k))
                                    # if not os.path.isdir(f"/home/chs.rintu/Documents/chs-lab-ws02/research-cancerPathology/histoImgSplit/OpenSlideGen/dataset/L{str(i)}/images"):
                                    #         os.makedirs(f"/home/chs.rintu/Documents/chs-lab-ws02/research-cancerPathology/histoImgSplit/OpenSlideGen/dataset/L{str(i)}/images")
                                    # im1 = deepzwsi.save(f"/home/chs.rintu/Documents/chs-lab-ws02/research-cancerPathology/histoImgSplit/OpenSlideGen/dataset/L{str(i)}/images/{str(i)}_{str(j)}_{str(k)}.jpg")
                                    if not os.path.isdir(f"/storage/bic/data/breastCancer/OpenSlideGenerator/dataset/{path.split('/')[-1].split('.')[0]}/L{str(i)}/images"):
                                            os.makedirs(f"/storage/bic/data/breastCancer/OpenSlideGenerator/dataset/{path.split('/')[-1].split('.')[0]}/L{str(i)}/images")
                                    if deepzwsi.size[0] < tile_size or deepzwsi.size[1] < tile_size:
                                        padded = np.ones((tile_size, tile_size, 3), dtype=np.uint8)
                                        padded *= 255
                                        deepzwsiarr = np.array(deepzwsi)
                                        padded[:deepzwsi.size[1], :deepzwsi.size[0], :] = deepzwsiarr
                                        deepzwsi = Image.fromarray(padded)
                                        im1 = deepzwsi.save(f"/storage/bic/data/breastCancer/OpenSlideGenerator/dataset/{path.split('/')[-1].split('.')[0]}/L{str(i)}/images/{str(i)}_{str(j)}_{str(k)}.jpg")
                                    else:
                                        im1 = deepzwsi.save(f"/storage/bic/data/breastCancer/OpenSlideGenerator/dataset/{path.split('/')[-1].split('.')[0]}/L{str(i)}/images/{str(i)}_{str(j)}_{str(k)}.jpg")
                    except:
                        print("Error in ", file)
                        continue



if __name__ == '__main__':
    folders = ["/storage/tnbc/OPTRASCAN_IISER_Round 11"  "/storage/tnbc/OPTRASCAN_IISER_Round_10",  "/storage/tnbc/OPTRASCAN_IISER_Round_2",  "/storage/tnbc/OPTRASCAN_IISER_Round_6",  "/storage/tnbc/OPTRASCAN_IISER_Round_8",  "/storage/tnbc/OPTRASCAN_IISER_Round_1",   "/storage/tnbc/OPTRASCAN_IISER_Round_12",  "/storage/tnbc/OPTRASCAN_IISER_Round_3",  "/storage/tnbc/OPTRASCAN_IISER_Round_7",  "/storage/tnbc/OPTRASCAN_IISER_Round_9" ]
    pool = Pool(mp.cpu_count())
    pool.map(list_creator, folders)
    pool.close()
    pool.join()

