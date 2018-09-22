#!/bin/bash


mode=$1

[ "$mode" == "persocket" ] && config="-a --per-socket" || config=""


for threads in 8 16 32 48 64
do
export OMP_NUM_THREADS=$threads

echo "Number of threads: $OMP_NUM_THREADS"
for size in '05' '1' '2' '5' '10' '20'
#for size in  '05'
        do
             perf stat $config  -e cycles,instructions,cache-references,cache-misses,faults,migrations /home/jlenis/numa_benchmark/bin/stream.$size''GiB.20 > /home/jlenis/numa_benchmark/outputs/stream/batcat/$threads/stream_NORMAL_batcat_$size''GB_$threads.secondround.txt &>$OMP_NUM_THREADS.$size.$mode.secondround.txt
        done
  done
  
