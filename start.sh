#! /bin/bash
#PBS -N OS-API-CSV
#PBS -o out.log
#PBS -e err.log
#PBS -l ncpus=100
#PBS -q cpu

module load compiler/anaconda3

conda init

source ~/.bashrc

conda activate openslide

python3 csv_generator.py

