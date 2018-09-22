#!/bin/bash
#SBATCH --job-name="stress batcat"
#SBATCH --exclusive
#SBATCH --mem=125G
#SBATCH -w batman
#SBATCH --time=40:00:00
#SBATCH --partition=p_hpca4se
#SBATCH -o /home/jlenis/numa_benchmark/outputs/numa_contention/batcat/stress_%j.log

##### Definition of enviromental variables #####
#export OMP_NUM_THREADS=16
export KMP_AFFINITY=verbose,none


echo "Number of threads: $OMP_NUM_THREADS"
echo "Job ID: $SLURM_JOB_ID"
echo "Machine: $SLURM_JOB_NODELIST "
################################################


##### Definition of variables #####
size=100
##mode=$2
counters="cycles,instructions,cache-references,cache-misses,faults,migrations"
output_path="/home/jlenis/numa_benchmark/outputs/numa_contention/batcat"
bin_path="/home/jlenis/numa_benchmark/bin/numa_contention"

/bin/mkdir -p "$output_path"


###################################
for threads in 8 16 32 48 64;
	do
	export OMP_NUM_THREADS=$threads 
		for node in 0 1 2 3 4 5 6 7;
		do
		for mode in 'amd' 'intel';
## perf stat $config -e $counters numactl   $bin_path/bench_stress $size $threads $node $mode  > $output_path'/'stress_bind_$SLURM_JOB_NODELIST'_'$size''GB_$OMP_NUM_THREADS''t_$mode'_'$SLURM_JOB_ID'.'txt
		do
		$bin_path/bench_stress $size $threads $node $mode  > $output_path/stress_bind_$SLURM_JOB_NODELIST'_'$size''MB_$OMP_NUM_THREADS''t_$mode'_'$node'_'$SLURM_JOB_ID'.'txt
		done
        done
done
