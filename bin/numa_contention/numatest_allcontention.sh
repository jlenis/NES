#!/bin/bash

tests='all_contention_argv'
sizes='62.5 125 250 500 1000 2000'
threads='8 16 32 48 64'
reps='1 2 3 4 5'
for test in $tests
do
    for size in $sizes
    do
        for thread in $threads
        do
            for rep in $reps
     	    do
    ./$test $size $thread  &> $test.$size.$thread.$rep.txt 
            done  
        done
     done
done 
