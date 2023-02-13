#! /bin/bash
#PBS -N OS-API-CSV
#PBS -o out.log
#PBS -e err.log
#PBS -l ncpus=50
#PBS -q cpu
#PBS -l host=compute3

module load compiler/anaconda3

conda init

source ~/.bashrc

conda activate openslide

python3 /storage/bic/data/breastCancer/OpenSlideGenerator/csv_generator.py

