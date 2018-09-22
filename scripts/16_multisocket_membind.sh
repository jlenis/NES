#!/bin/bash
#SBATCH --job-name="membind 16 batcat"
#SBATCH --exclusive
#SBATCH --mem=125G
##SBATCH -w catwoman
#SBATCH --time=40:00:00
#SBATCH --partition=p_hpca4se
#SBATCH -o /home/jlenis/numa_benchmark/outputs/stream/batcat/16/membind_16_batcat_%j.log
#SBATCH -C "Opteron"

##### Definition of enviromental variables #####
export OMP_NUM_THREADS=16
export KMP_AFFINITY=verbose,none


echo "Number of threads: $OMP_NUM_THREADS"
echo "Job ID: $SLURM_JOB_ID"
echo "Machine: $SLURM_JOB_NODELIST "
################################################


##### Definition of variables #####
size=$1
mode=$2
counters="cycles,instructions,cache-references,cache-misses,faults,migrations"
output_path="/home/jlenis/numa_benchmark/outputs/stream/batcat/$OMP_NUM_THREADS/$1"
bin_path="/home/jlenis/numa_benchmark/bin"

/bin/mkdir -p "$output_path"

[ "$mode" == "amb" ] && config="-a --per-socket" || config=""

###################################

	        for socket2 in 0 1 2 3 4 5 6 7;
   	            do
    	                for socket in 0 1 2 3 4 5 6 7;
       	                    do
                                if (($socket <  $socket2 ));
		                     then
                	                 for node in  0 1 2 3 4 5 6 7;
                  	                     do
	 		    	                 start2=$SECONDS
	 			                     echo "Socket: $socket,$socket2  MEM: $node"
         			                     
                                                     perf stat $config -e $counters numactl --cpunodebind=$socket,$socket2 --membind=$node  $bin_path/stream.$size''GiB.10 > $output_path'/'stream_membind_$SLURM_JOB_NODELIST'_'$size''GB_proc$socket-$socket2'_'mem$node'_'$OMP_NUM_THREADS''t_$mode'_'$SLURM_JOB_ID'.'txt
	 			                     end=$SECONDS
         			                     runtime=$((end-start2))
			                     done
                                     fi
	                        echo " Time Elapsed: $runtime"
                            done
                    done
