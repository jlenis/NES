#!/bin/bash

for size in '05' '1' '2' '5'
    do 
        for mode in amb sense
            do
			echo "sbatch 8_multisocket.sh $size $mode " 
			#sbatch 8_multisocket.sh $size $mode 
            
            done
    done

	for size in '05' '1' '2' '5'
    do 
        for mode in amb sense
            do
                echo "sbatch 16_multisocket_interleave.sh $size $mode "
	        	#sbatch 16_multisocket_interleave.sh $size $mode
                echo "sbatch 16_multisocket_membind.sh $size $mode "
			#sbatch 16_multisocket_membind.sh $size $mode    
            done
    done

	for size in '05' '1' '2' '5'
    do 
        for mode in amb sense
            do
                
			echo "sbatch 32_multisocket_interleave.sh $size $mode "
			#sbatch 32_multisocket_interleave.sh $size $mode
			echo "sbatch 32_multisocket_membind.sh $size $mode "
			sbatch 32_multisocket_membind.sh $size $mode
		           
            done
    done
