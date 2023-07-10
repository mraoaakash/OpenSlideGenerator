from math import log10
import openslide
from openslide.deepzoom import DeepZoomGenerator
import numpy as np
import os
from multiprocessing import Pool
import multiprocessing as mp 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from PIL import Image

key = {
    "20210821_720_358_19_1250_19_A_ER_biopsy_HnE_40X":"ICGA-0001-00001-001-001-040-0001",
    "20210821_719_353_19_1320_19_B_HER2_biopsy_HnE_40X":"ICGA-0001-00002-001-001-040-0001",
    "20200220-317-270_14-G_14_4036C-TNBC-Surgery-HnE-40X":"ICGA-0001-00003-001-001-040-0001",
}
inpath = "/media/chs.ccb/06b46169-9931-4457-aba6-c50c11d77e3d/researchxBreastCancer/temp"
outpath = "/media/chs.ccb/06b46169-9931-4457-aba6-c50c11d77e3d/researchxBreastCancer/out"

def getTiles(img):
    tile_size = 256
    image = openslide.OpenSlide(img)
    dzoomImg = DeepZoomGenerator(image, tile_size=tile_size, overlap=0, limit_bounds=True)
    print(dzoomImg.level_dimensions)
    for i in range(9,dzoomImg.level_count):    
        leveltiles = dzoomImg.level_tiles[i]
        print(f'leveltiles_{i} : {leveltiles}')
        for j in range(0,leveltiles[0]):
            for k in range(0,leveltiles[1]):
                deepzwsi = dzoomImg.get_tile(i, address = (j, k))
                if not os.path.isdir(f"{outpath}/{key[img.split('/')[-1].split('.')[0]]}/L{str(i)}/images"):
                        os.makedirs(f"{outpath}/{key[img.split('/')[-1].split('.')[0]]}/L{str(i)}/images")
                if deepzwsi.size[0] < tile_size or deepzwsi.size[1] < tile_size:
                    padded = np.ones((tile_size, tile_size, 3), dtype=np.uint8)
                    padded *= 255
                    deepzwsiarr = np.array(deepzwsi)
                    padded[:deepzwsi.size[1], :deepzwsi.size[0], :] = deepzwsiarr
                    deepzwsi = Image.fromarray(padded)
                    im1 = deepzwsi.save(f"{outpath}/{key[img.split('/')[-1].split('.')[0]]}/L{str(i)}/images/{str(i)}_{str(j)}_{str(k)}.tif")
                else:
                    im1 = deepzwsi.save(f"{outpath}/{key[img.split('/')[-1].split('.')[0]]}/L{str(i)}/images/{str(i)}_{str(j)}_{str(k)}.tif")

def stats(path, sizes):
    file_sizes = [[0 for i in range(18)]for j in range(len(sizes))]
    for i in range(len(sizes)):
        for j in range(18):
            file_sizes[i][j] = len(os.listdir(f"{path}/{sizes[i]}/level{j}"))
    print(file_sizes)
    file_sizes = pd.DataFrame(file_sizes, index=sizes, columns=[str(i) for i in range(18)])
    print(file_sizes)
    plt.figure(figsize=(10, 5))
    sns.heatmap(file_sizes, annot=True, fmt="d",annot_kws={'rotation': 45})
    plt.xlabel("Level")
    plt.ylabel("Tile Size")
    plt.title("Number of Tiles")
    plt.tight_layout()
    plt.savefig(f"{path}/stats.png")

def textGen(path):
    with open(f'{path}/images.txt', 'w+') as fp:
        for item in os.listdir(f'{path}/images'):
            # write each item on a new line
            if item.endswith(".jpg"):
                fp.write("%s\n" % item)
        print('Done')
    return 0



if __name__ == '__main__':
    tile_size = [256] # originally [256, 512, 1024]
    pool = Pool(mp.cpu_count())
    imgs = []
    for i in os.listdir(f"/{inpath}"):
        imgs.append(f'/{inpath}/{i}')
        print(i)
    imgs = imgs[0:1]
    pool.map(getTiles, imgs)
    pool.close()
    pool.join()  
    # stats("/home/chs.rintu/Documents/chs-lab-ws02/research-cancerPathology/histoImgSplit/OpenSlideGen", i)
    # stats("/storage/bic/data/breastCancer/OpenSlideGenerator", [256, 512, 1024])
    # textGen("/home/chs.rintu/Documents/chs-lab-ws02/research-cancerPathology/histoImgSplit/OpenSlideGen/images")
    # for i in range(9, 18):
    #     textGen(f"/storage/bic/data/breastCancer/OpenSlideGenerator/dataset/L{i}")
    # pass
