#!/bin/bash

export OMP_NUM_THREADS=64

echo "Number of threads: $OMP_NUM_THREADS"
for size in '05' '1' '2' '5'
        do
             perf stat  -e cycles,instructions,cache-references,cache-misses,faults,migrations /home/jlenis/numa_benchmark/bin/stream.$size''GiB.10 > /home/jlenis/numa_benchmark/outputs/stream/batcat/64/stream_NORMAL_batcat_$size''GB_64t.tx
        done
  
  
