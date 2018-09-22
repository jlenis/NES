#!/bin/bash


gcc -fopenmp -mcmodel=medium -O0 -DSTREAM_ARRAY_SIZE=65536000 -DNTIMES=10 stream.c -o stream.05GiB.10.worst
gcc -fopenmp -mcmodel=medium -O0 -DSTREAM_ARRAY_SIZE=131072000 -DNTIMES=10 stream.c -o stream.1GiB.10.worst
gcc -fopenmp -mcmodel=medium -O0 -DSTREAM_ARRAY_SIZE=262144000 -DNTIMES=10 stream.c -o stream.2GiB.10.worst
gcc -fopenmp -mcmodel=medium -O0 -DSTREAM_ARRAY_SIZE=524288000 -DNTIMES=10 stream.c -o stream.4GiB.10.worst
gcc -fopenmp -mcmodel=medium -O0 -DSTREAM_ARRAY_SIZE=1048576000 -DNTIMES=10 stream.c -o stream.8GiB.10.worst
gcc -fopenmp -mcmodel=medium -O0 -DSTREAM_ARRAY_SIZE=2097152000 -DNTIMES=10 stream.c -o stream.16GiB.10.worst

gcc -fopenmp -mcmodel=medium -O0 -DSTREAM_ARRAY_SIZE=65536000 -DNTIMES=20 stream.c -o stream.05GiB.20.worst
gcc -fopenmp -mcmodel=medium -O0 -DSTREAM_ARRAY_SIZE=131072000 -DNTIMES=20 stream.c -o stream.1GiB.20.worst
gcc -fopenmp -mcmodel=medium -O0 -DSTREAM_ARRAY_SIZE=262144000 -DNTIMES=20 stream.c -o stream.2GiB.20.worst
gcc -fopenmp -mcmodel=medium -O0 -DSTREAM_ARRAY_SIZE=524288000 -DNTIMES=20 stream.c -o stream.4GiB.20.worst
gcc -fopenmp -mcmodel=medium -O0 -DSTREAM_ARRAY_SIZE=1048576000 -DNTIMES=20 stream.c -o stream.8GiB.20.worst
gcc -fopenmp -mcmodel=medium -O0 -DSTREAM_ARRAY_SIZE=2097152000 -DNTIMES=20 stream.c -o stream.16GiB.20.worst


gcc -fopenmp -mcmodel=medium -march=core2 -mtune=amdfam10 -DSTREAM_ARRAY_SIZE=65536000 -DNTIMES=10 stream.c -o stream.05GiB.10.best
gcc -fopenmp -mcmodel=medium -march=core2 -mtune=amdfam10 -DSTREAM_ARRAY_SIZE=131072000 -DNTIMES=10 stream.c -o stream.1GiB.10.best
gcc -fopenmp -mcmodel=medium -march=core2 -mtune=amdfam10 -DSTREAM_ARRAY_SIZE=262144000 -DNTIMES=10 stream.c -o stream.2GiB.10.best
gcc -fopenmp -mcmodel=medium -march=core2 -mtune=amdfam10 -DSTREAM_ARRAY_SIZE=524288000 -DNTIMES=10 stream.c -o stream.4GiB.10.best
gcc -fopenmp -mcmodel=medium -march=core2 -mtune=amdfam10 -DSTREAM_ARRAY_SIZE=1048576000 -DNTIMES=10 stream.c -o stream.8GiB.10.best
gcc -fopenmp -mcmodel=medium -march=core2 -mtune=amdfam10 -DSTREAM_ARRAY_SIZE=2097152000 -DNTIMES=10 stream.c -o stream.16GiB.10.best

gcc -fopenmp -mcmodel=medium -march=core2 -mtune=amdfam10 -DSTREAM_ARRAY_SIZE=65536000 -DNTIMES=20 stream.c -o stream.05GiB.20.best
gcc -fopenmp -mcmodel=medium -march=core2 -mtune=amdfam10 -DSTREAM_ARRAY_SIZE=131072000 -DNTIMES=20 stream.c -o stream.1GiB.20.best
gcc -fopenmp -mcmodel=medium -march=core2 -mtune=amdfam10 -DSTREAM_ARRAY_SIZE=262144000 -DNTIMES=20 stream.c -o stream.2GiB.20.best
gcc -fopenmp -mcmodel=medium -march=core2 -mtune=amdfam10 -DSTREAM_ARRAY_SIZE=524288000 -DNTIMES=20 stream.c -o stream.4GiB.20.best
gcc -fopenmp -mcmodel=medium -march=core2 -mtune=amdfam10 -DSTREAM_ARRAY_SIZE=1048576000 -DNTIMES=20 stream.c -o stream.8GiB.20.best
gcc -fopenmp -mcmodel=medium -march=core2 -mtune=amdfam10 -DSTREAM_ARRAY_SIZE=2097152000 -DNTIMES=20 stream.c -o stream.16GiB.20.best
