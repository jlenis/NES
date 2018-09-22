import re
import csv
import numpy as np
import os
import fnmatch


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                return name





def stream_parser():
    # # cwd = os.getcwd()
    exist_file = False
    cwd = os.path.dirname(os.getcwd())
    sizes = ['05', '1', '2', '5', '10', '20']
    modes = ['wide']
    threads_set = [8, 16, 32, 48, 64]

    for mode in modes:
        route = '{}/outputs/stream/batcat/regular/secondround/'.format(cwd, mode)
        with open(route + '{}.secondround.csv'.format(mode), 'w') as csvfile:
            os.chdir(route) 
            results_writer = csv.writer(csvfile, dialect='excel')
            results_writer.writerow(['Name', 8, 16, 32, 48, 64])

            for size in sizes:
                results_writer.writerow(['', size, size, size, size, size])
                perf_counters = {'cycles': ['cycles'], 'instructions': ['instructions'], 'cache-misses': ['cache-misses'], 'cache-references': ['cache-references'], 'faults'
                            : ['faults'], 'migrations': ['migrations'], 'seconds time elapsed': ['time']}

                stream_counters = {'Copy': ['copy'], 'Scale': ['scale'], 'Add': ['add'], 'Triad': ['triad']}

                for threads in threads_set:
                    name = '{}.{}.{}.secondround.txt'.format(threads, size, mode)
                    name_file = find(name, route)

                    if name_file is not None:
                        exist_file = True
                        print('Opening ', name_file)
                        file = open(route + name_file, 'r')

                        for line in file:
                            for key in stream_counters:
                                if re.search(key, line):
                                    line_bw = line.replace('\n', '')
                                    line_bw = line_bw.split(' ')
                                    line_bw = [x for x in line_bw if x != '']
                                    stream_counters[key].append(line_bw[1])
                                    print(key, stream_counters[key])

                            for key in perf_counters.keys():
                                if re.search(key, line):
                                    line_counter = line.split(" ")
                                    line_counter = [x for x in line_counter if x != '']
                                    perf_counters[key].append(line_counter[0])
                                    print(key, perf_counters[key])
                    else:
                        exist_file = False

                if exist_file:
                    for key in stream_counters:
                        results_writer.writerow(stream_counters[key])
                    for key in perf_counters:
                        results_writer.writerow(perf_counters[key])



def main():
    stream_parser()


if __name__ == "__main__":
    main()