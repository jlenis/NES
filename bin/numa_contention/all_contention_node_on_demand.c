//
// Created by Jo Lenis on 23/07/2018.
//

// Based on numatest.cpp by James Brock
// http://stackoverflow.com/questions/7259363/measuring-numa-non-uniform-memory-access-no-observable-asymmetry-why
//
// Changes by Andreas Kloeckner, 10/2012:
// - Rewritten in C + OpenMP
// - Added contention tests

#define _GNU_SOURCE

#include <numa.h>
#include <sched.h>
#include <stdio.h>
#include <pthread.h>
#include <omp.h>
#include <assert.h>
#include "timing.h"
#include <string.h>

void pin_to_core(size_t core) {
    cpu_set_t cpuset;
    CPU_ZERO(&cpuset);
    CPU_SET(core, &cpuset);
    pthread_setaffinity_np(pthread_self(), sizeof(cpu_set_t), &cpuset);
}

void print_bitmask(const struct bitmask *bm) {
    for (size_t i = 0; i < bm->size; ++i)
        printf("%d", numa_bitmask_isbitset(bm, i));
}


double measure_access(void *x, size_t array_size, size_t ntrips) {
    timestamp_type t1;
    get_timestamp(&t1);

    for (size_t i = 0; i < ntrips; ++i)
        for (size_t j = 0; j < array_size; ++j) {
            *(((char *) x) + ((j * 8009) % array_size)) += 1;
        }

    timestamp_type t2;
    get_timestamp(&t2);

    return timestamp_diff_in_seconds(t1, t2);
}

int main(int argc, char *argv[]) {
    if (argc < 3) {
        printf("usage: bench size[MB] num_cpus node pin_mode[scatter | gather]\n");
        return 0;
    }
    long size = strtol(argv[1], NULL, 10);
    // int num_cpus = numa_num_task_cpus();
    long num_cpus = strtol(argv[2], NULL, 10);

    long node = strtol(argv[3], NULL, 10);
    
    char pin_mode[5];
    strcpy(pin_mode,argv[4]);


    int order[64];

    if (strcmp(pin_mode, "amd") == 0 ) {
        printf("entra aquí");
	for (int j = 0; j < num_cpus; j++) {
            order[j] = j;
        }
    } else {
        int i = 0;
        for (int j = 0; j < 4; j++) {
            for (int k = 0; k < 16; k++) {
                order[i] = j + k * 4;
                i++;

            }
        }
    }
    
    printf("Architecture: %s\n", pin_mode);
    printf("num cpus: %d\n", num_cpus);

    printf("numa available: %d\n", numa_available());
    //numa_set_localalloc();

    /*for (int h=0; h < num_cpus; h++){
	printf("order[%d] = %d\n", h, order[h]);
	}
    */
    /*
    struct bitmask *bm = numa_bitmask_alloc(num_cpus);


    /* numa_bitmask_alloc() allocates a bitmask structure and its associated bit mask.
     The memory allocated for the bit mask contains enough words (type unsigned long) to contain n bits.
     The bit mask is zero-filled. The bitmask structure points to the bit mask and contains the n value.
    */
    // print_bitmask(bm);
  /*  for (int i = 0; i <= numa_max_node(); ++i) {
        numa_node_to_cpus(i, bm);



        /*numa_node_to_cpus converts a node number to a bitmask of CPUs. The user must pass a bitmask structure
         with a mask buffer long enough to represent all possible cpu's. Use numa_allocate_cpumask() to create it.
         If the bitmask is not long enough errno will be set to ERANGE and -1 returned. On success 0 is returned.
         */
/*
        printf("numa node %d ", i);
        print_bitmask(bm);
        printf(" - %g GiB\n", numa_node_size(i, 0) / (1024. * 1024 * 1024.));
    }
    numa_bitmask_free(bm);

    puts("");
    */
    char *x;
    const size_t cache_line_size = 64;
    const size_t array_size = size * 1024 * 1024;
    size_t ntrips = 2;

    printf("array size: %d \n", array_size * sizeof(char));
#pragma omp parallel
    {
        //assert(omp_get_num_threads() == num_cpus);
        int tid = omp_get_thread_num();
	//printf("\n thread %d - core %d", tid, order[tid]);
        pin_to_core(order[tid]);
        if (tid == 0) {
            x = (char *) numa_alloc_onnode(array_size, node);
            printf("x size: %d \n", sizeof(x) * array_size);
        }
        // {{{ everybody contends for one

        {
            if (tid == 0) puts("");

#pragma omp barrier
            double t = measure_access(x, array_size, ntrips);
#pragma omp barrier
            for (size_t i = 0; i < num_cpus; ++i) {
                if (tid == i)
                    printf("all-contention tid: %d  core %d -> core 0 : BW %g MB/s\n",
                           tid, order[tid], array_size * ntrips * cache_line_size / t / 1e6);
#pragma omp barrier
            }
        }
        // }}}

        // {{{ zero and someone else contending

    }
    numa_free(x, array_size);

    return 0;
}
