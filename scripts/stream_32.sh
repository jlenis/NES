#!/bin/bash
#SBATCH --job-name="stream 32t batcat"
#SBATCH --exclusive
#SBATCH --mem=125G
##SBATCH -w batcat
#SBATCH --time=40:00:00
#SBATCH --partition=p_hpca4se
#SBATCH -o /home/jlenis/numa_benchmark/outputs/stream/batcat/32/stream_regular_32t_batcat_%j.log
#SBATCH -C "Opteron"

##### Definition of enviromental variables #####
export OMP_NUM_THREADS=32
export KMP_AFFINITY=verbose,none


echo "Number of threads: $OMP_NUM_THREADS"
echo "Job ID: $SLURM_JOB_ID"
echo "Machine: $SLURM_JOB_NODELIST "
################################################


##### Definition of variables #####
size=$1
counters="cycles,instructions,cache-references,cache-misses,faults,migrations"
output_path="/home/jlenis/numa_benchmark/outputs/stream/batcat/$OMP_NUM_THREADS/$size"
bin_path="/home/jlenis/numa_benchmark/bin"




###################################

echo "$runtime"

 perf stat $config -e $counters $bin_path/stream.$size''GiB.10 > $output_path'/'stream_NORMAL_$SLURM_JOB_NODELIST'_'$size'GB_'$OMP_NUM_THREADS't_'$SLURM_JOB_ID'.'txt
  
  
