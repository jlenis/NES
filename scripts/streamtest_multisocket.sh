#!/bin/bash


start=`date +%s`
sleep 10
end=`date +%s`

runtime=$((end-start))

echo "$runtime"


export OMP_NUM_THREADS=16
echo "Number of threads: $OMP_NUM_THREADS"
for socket in 0 1 2 3 4 5 6 7
  do    
    for node in  0 1 2 3 4 5 6 7
       do 
	 start="date +%s"
	 echo "Socket: 0,$socket  MEM: $node"
         numactl --cpunodebind=0,$socket --membind=$node  ./stream.1GiB.20 > nodebind0-$socket.membind$node.16t.txt
	 end="date +%s"
         runtime=$((end-start))

	 echo " Time Elapsed: $runtime"
       done
  done
