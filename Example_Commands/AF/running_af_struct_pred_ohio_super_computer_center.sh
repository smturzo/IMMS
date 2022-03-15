#!/bin/bash
#SBATCH --account=PAS1146
#SBATCH --job-name=1KTU_AF
#SBATCH --time=08:00:00
#SBATCH --nodes=1 --ntasks=48
#SBATCH --gpus-per-node=1
#SBATCH --error=error.txt
#SBATCH --output=log.txt
#SBATCH --mail-user=turzo.1@osu.edu
#SBATCH --mail-type=END,FAIL
set -vx
module reset
module load alphafold/2.0.0

run_alphafold.sh --preset=full_dbs --fasta_paths=1KTU_A.fasta --max_template_date=2002-01-16 --output_dir=./
