#!/bin/bash

for threads in 1 8 64
  do
    export OMP_NUM_THREADS=$threads
    echo "Number of threads: $OMP_NUM_THREADS"
    for node in  0 1 2 3 4 5 6 7
       do 
	 echo "Socket: 0 MEM: $node"
         numactl --cpunodebind=0 --membind=$node  ./stream.1GiB.20 > nodebind0_membind$node.$threads.t.txt
       done
  done
