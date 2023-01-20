import os
from multiprocessing import Pool
import multiprocessing as mp
import openslide
from openslide.deepzoom import DeepZoomGenerator

def list_creator(path):
    for dirs, subdirs, files in os.walk(path):
        for file in files:
            if file.endswith('.tif'):
                if "HNE" in file.upper():
                    print(file)
                    try:
                        image = openslide.OpenSlide(os.path.join(dirs, file))
                        # print(image.dimensions)
                        dzoomImg = DeepZoomGenerator(image, tile_size=256, overlap=0, limit_bounds=True)
                        print(dzoomImg.level_count)
                        print(dzoomImg.level_tiles)
                        print(dzoomImg.level_dimensions)
                    except:
                        print("Error in ", file)
                        continue


if __name__ == '__main__':
    folders = ["/storage/tnbc/OPTRASCAN_IISER_Round 11"  "/storage/tnbc/OPTRASCAN_IISER_Round_10",  "/storage/tnbc/OPTRASCAN_IISER_Round_2",  "/storage/tnbc/OPTRASCAN_IISER_Round_6",  "/storage/tnbc/OPTRASCAN_IISER_Round_8",  "/storage/tnbc/OPTRASCAN_IISER_Round_1",   "/storage/tnbc/OPTRASCAN_IISER_Round_12",  "/storage/tnbc/OPTRASCAN_IISER_Round_3",  "/storage/tnbc/OPTRASCAN_IISER_Round_7",  "/storage/tnbc/OPTRASCAN_IISER_Round_9" ]
    pool = Pool(mp.cpu_count())
    pool.map(list_creator, folders)
    pool.close()
    pool.join()

