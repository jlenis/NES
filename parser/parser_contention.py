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


def contention_parser():
    # # cwd = os.getcwd()
    exist_file = False
    cwd = os.path.dirname(os.getcwd())
    archs = ['penguin', 'batman']
    modes = ['intel', 'amd']
    threads = [8, 16, 32, 48, 64]
    for mode in modes:

        for arch in archs:
            if arch == 'penguin':
                nodes = 4
            else:
                nodes = 8

            route = '{}/outputs/numa_contention/{}/'.format(cwd, arch)

            if (arch == 'penguin' and mode == 'amd') or (arch == 'batman' and mode == 'intel'):
                style = 'sparse'
            else:
                style = 'dense'

            for thread in threads:

                with open(route + 'contention_{}_{}_{}.csv'.format(arch, style, thread), 'w') as csvfile:
                    os.chdir(route)
                    results_writer = csv.writer(csvfile, dialect='excel')
                    results_writer.writerow(['tid', 'core', 'node', 'bw'])
                    for node in range(0, int(nodes)):
                        # stream_membind_batman_1GB_proc0_mem0_8t_sense_1936
                        name = 'stress_bind_{}_100MB_{}t_{}_{}_*'.format(arch, thread, mode, node)
                        # name = 'stream_membind_{}_{}GB_proc{}_mem{}_{}t_{}*'.format(arch, size, socket, node, threads,
                        #                                                             mode)
                        line_to_write = list()
                        # average.append(node)
                        name_file = find(name, route)
                        if name_file is not None:
                            print('Opening ', name_file)
                            file = open(route + name_file, 'r')
                            for line in file:
                                if re.search('all-contention', line):
                                    line_processed = line.replace('\n', '')
                                    line_processed = line_processed.split(' ')
                                    line_processed = [x for x in line_processed if x != '']
                                    # line_to_write.append()
                                    print("Line found: ", line_processed)
                                    # results_writer.writerow(line_exec_time)
                                    print([line_processed[2], line_processed[4], node, line_processed[10]])
                                    results_writer.writerow(
                                        [line_processed[2], line_processed[4], node, line_processed[10]])
                                    # mean = np.mean(
                                    #     [float(matrix_file[0][1]), float(matrix_file[1][1]), float(matrix_file[2][1]),
                                    #      float(matrix_file[3][1])]) * 1.7
                                    # average.append(mean)
                                    #
                csvfile.close()


def main():
    # print("Welcome to results parser")
    # sockets = input("How many sockets? ")
    # nodes = input("How many memory nodes? ")
    # threads = input("How many threads? ")
    # arch = 'penguin'
    # if arch == 'penguin':
    #     sockets = nodes = 4
    # else:
    #     sockets = nodes = 8

    contention_parser()


if __name__ == "__main__":
    main()
