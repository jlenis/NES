echo "perf stat $config -e $counters numactl --cpunodebind=$socket --membind=$node $bin_path/stream.$1""GiB.20"
