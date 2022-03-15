#!/bin/bash
#SBATCH --account=PAS1146
#SBATCH --job-name=6AZZ_HMR
#SBATCH --time=65:00:00
#SBATCH --nodes=3 --ntasks-per-node=40
#SBATCH --error=error.txt
#SBATCH --output=log.txt
#SBATCH --mail-user=turzo.1@osu.edu
#SBATCH --mail-type=END,FAIL
set -vx
module load rosetta/3.12
module load pcp/pcp
srun parallel-command-processor relax_starter
