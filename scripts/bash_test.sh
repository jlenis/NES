#!/bin/bash
start=`date +%s`
sleep 10
end=`date +%s`

runtime=$((end-start))

echo "$runtime"
