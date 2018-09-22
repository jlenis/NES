#!/bin/bash
#SBATCH --job-name="pchase penguin"
#SBATCH --exclusive
#SBATCH --mem=125G
##SBATCH -w penguin
#SBATCH --time=40:00:00
#SBATCH --partition=p_hpca4se
#SBATCH -o /home/jlenis/numa_benchmark/outputs/pchase/pchase_penguin_%j.log

##### Definition of enviromental variables #####

echo "Number of threads: $OMP_NUM_THREADS"
echo "Job ID: $SLURM_JOB_ID"
echo "Machine: $SLURM_JOB_NODELIST "
################################################
echo "$runtime"

source $HOME/.bash_profile

echo $PATH

/home/jlenis/numa_benchmark/bin/others/pChase/scripts/test-memory.sh

  
  
