#!/bin/bash
#SBATCH --job-name="pchase batcat"
#SBATCH --exclusive
#SBATCH --mem=125G
##SBATCH -w batman
#SBATCH --time=40:00:00
#SBATCH --partition=p_hpca4se
#SBATCH -o /home/jlenis/numa_benchmark/outputs/pchase/pchase_batcat_%j.log
#SBATCH -C "Opteron"

##### Definition of enviromental variables #####

echo "Number of threads: $OMP_NUM_THREADS"
echo "Job ID: $SLURM_JOB_ID"
echo "Machine: $SLURM_JOB_NODELIST "
################################################
echo "$runtime"

source $HOME/.bash_profile

echo $PATH

/home/jlenis/numa_benchmark/bin/others/pChase/scripts/test-memory.sh

  
  
