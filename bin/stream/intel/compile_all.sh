#!/bin/bash

icc -O3 -xCORE-AVX2 -ffreestanding -openmp -DSTREAM_ARRAY_SIZE=400000000 stream.c
