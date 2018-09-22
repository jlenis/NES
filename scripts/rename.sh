

#!/bin/bash
declare -a pruebas=("forward" "memcpy" "backward" "ptrchase" "random2" "stream")

declare -a dimensiones=("1GB" "100MB")

for prueba in "${pruebas[@]}"
    do
        for dimension in "${dimensiones[@]}"
            do 
		rename numademo_.$prueba_$dimension "numademo_$prueba_batman_$dimension" numademo* 
	   done
   done
