import os
from multiprocessing import Pool
import multiprocessing as mp

def list_creator(path):
    for dirs, subdirs, files in os.walk(path):
        for file in files:
            if file.endswith('.tif'):
                if "HNE" in file.upper():
                    print("HNE")

if __name__ == '__main__':
    folders = ["/storage/tnbc/OPTRASCAN_IISER_Round 11"  "/storage/tnbc/OPTRASCAN_IISER_Round_10",  "/storage/tnbc/OPTRASCAN_IISER_Round_2",  "/storage/tnbc/OPTRASCAN_IISER_Round_6",  "/storage/tnbc/OPTRASCAN_IISER_Round_8",  "/storage/tnbc/OPTRASCAN_IISER_Round_1",   "/storage/tnbc/OPTRASCAN_IISER_Round_12",  "/storage/tnbc/OPTRASCAN_IISER_Round_3",  "/storage/tnbc/OPTRASCAN_IISER_Round_7",  "/storage/tnbc/OPTRASCAN_IISER_Round_9" ]
    pool = Pool(mp.cpu_count())
    pool.map(list_creator, folders)