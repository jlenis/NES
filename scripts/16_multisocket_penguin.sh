#!/bin/bash

echo "$runtime"

export OMP_NUM_THREADS=16
echo "Number of threads: $OMP_NUM_THREADS"
for socket in 0 1 2 3 4 5 6 7
  do    
    for node in  0 1 2 3 4 5 6 7
       do 
	 start=`date +%s`
	 echo "Socket: $socket  MEM: $node"
         numactl --cpunodebind=$socket --interleave=0,$node  ./stream.1GiB.20 > nodebind$socket.interleave0-$node.$OMP_NUM_THREADS.t.txt
	 end=`date +%s`
         runtime=$((end-start))

	 echo " Time Elapsed: $runtime"
       done
  done
