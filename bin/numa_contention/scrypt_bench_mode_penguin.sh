#!/bin/bash
#SBATCH --job-name="contention penguin"
#SBATCH --exclusive
#SBATCH --mem=125G
#SBATCH -w penguin
#SBATCH --time=40:00:00
#SBATCH --partition=p_hpca4se
#SBATCH -o /home/jlenis/numa_benchmark/bin/numa_contention/penguin/%j.log


nodes='0 1 2 3 '
nodes_reverse='3 2 1 0' 
tries='1 2 3 4 5'

for node in $nodes;do
	for try in $tries;do
    		./bench_node 100 64 $node  > penguin/bench_node.$node.$try.txt
	done
done

for node in $nodes_reverse;do
	for attempt in $tries;do	
		./bench_node 100 64 $node  > penguin/bench_node.$node.$attempt.R.txt
	done
done
