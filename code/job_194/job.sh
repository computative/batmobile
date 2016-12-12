#!/bin/bash
#SBATCH --partition=normal 
#SBATCH --nodes=18 
#SBATCH --ntasks-per-node=8 
#SBATCH --time=1:00:00 
#SBATCH --job-name=batmobile 
mpirun ./batman 72 
