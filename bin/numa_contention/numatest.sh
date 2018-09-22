#!/bin/bash

tests='all_contention  single_thread'
sizes='100 1000'

for test in $tests
do
  for size in $sizes
  do
    ./$test $size > $test.$size.txt 
  done
done 
