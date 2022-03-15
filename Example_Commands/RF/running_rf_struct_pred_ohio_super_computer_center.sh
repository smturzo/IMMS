#!/bin/bash
#SBATCH --account=PAS1146
#SBATCH --job-name=1KTU_RTTA
#SBATCH --time=08:00:00
#SBATCH --nodes=1 --ntasks=48
#SBATCH --gpus-per-node=1
#SBATCH --error=error.txt
#SBATCH --output=log.txt
#SBATCH --mail-user=turzo.1@osu.edu
#SBATCH --mail-type=END,FAIL
set -vx
module reset
module load python/3.7-2019.10
module load cuda/10.0.130
source activate RoseTTAFold
/fs/project/PAS1146/turzo.1/RoseTTAFold/run_e2e_ver.sh ./1KTU_A.fasta ./
