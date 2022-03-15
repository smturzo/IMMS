#!/bin/bash
#SBATCH --account=PAS1146
#SBATCH --job-name=1KTU_EX_R
#SBATCH --time=80:00:00
#SBATCH --nodes=5 --ntasks-per-node=25
#SBATCH --error=error.txt
#SBATCH --output=log.txt
#SBATCH --mail-user=turzo.1@osu.edu
#SBATCH --mail-type=END,FAIL
set -vx
module load rosetta/3.12
module load pcp/pcp
srun parallel-command-processor relax_starter
