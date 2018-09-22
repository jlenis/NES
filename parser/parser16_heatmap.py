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


def stream_parser(sockets, nodes, threads, arch):
    # # cwd = os.getcwd()
    exist_file = False
    cwd = os.path.dirname(os.getcwd())
    sizes = ['05', '1', '2', '5']
    modes = ['amb', 'sense']
    experiments = ['interleave', 'membind']

    for size in sizes:
        for mode in modes:
            route = '{}/outputs/stream/{}/{}/{}/'.format(cwd, arch, threads, size)
            for experiment in experiments:
                with open(route + '{}_{}_heatmap_wcorrected.csv'.format(mode, experiment), 'w') as csvfile:
                    os.chdir(route)
                    results_writer = csv.writer(csvfile, dialect='excel')
                    results_writer.writerow(['processor', 'node', 'bw'])

                    for socket1 in range(0, int(sockets)):
                        for socket2 in range(0, int(sockets)):
                            if socket1 < socket2:
                                for node in range(0, int(nodes)):
                                    average = [str(socket1) + '-' + str(socket2)]
                                    average.append(node)
                                    # stream_membind_batman_1GB_proc0_mem0_8t_sense_1936
                                    if experiment == 'membind':
                                        name = 'stream_{}_{}_{}GB_proc{}-{}_mem{}_{}t_{}*'.format(experiment, arch,
                                                                                                  size, socket1,
                                                                                                  socket2, node,
                                                                                                  threads, mode)
                                    else:
                                        name = 'stream_{}_{}_{}GB_proc{}-{}_mem0-{}_{}t_{}*'.format(experiment, arch,
                                                                                                    size,
                                                                                                    socket1,
                                                                                                    socket2, node,
                                                                                                    threads, mode)

                                    name_file = find(name, route)
                                    if name_file is not None:
                                        exist_file = True
                                        # print('Opening ', name_file)
                                        file = open(route + name_file, 'r')
                                        matrix_file = list()
                                        for line in file:
                                            if re.search('Copy', line) or re.search('Scale', line) or re.search('Add',
                                                                                                                line) \
                                                    or re.search('Triad', line):
                                                line_exec_time = line.replace('\n', '')
                                                line_exec_time = line_exec_time.split(' ')
                                                line_exec_time = [x for x in line_exec_time if x != '']
                                                matrix_file.append(line_exec_time)
                                                print("Line found: ", line_exec_time)
                                                # results_writer.writerow(line_exec_time)

                                        mean = np.mean([float(matrix_file[0][1]), float(matrix_file[1][1]),
                                                        float(matrix_file[2][1]), float(matrix_file[3][1])])
                                        average.append(mean)
                                        results_writer.writerow(average)


def main():
    # print("Welcome to results parser")
    # sockets = input("How many sockets? ")
    # nodes = input("How many memory nodes? ")
    # threads = input("How many threads? ")
    threads = input("How many threads? ")
    arch = 'batcat'
    if arch == 'penguin':
        sockets = nodes = 4
    else:
        sockets = nodes = 8

    stream_parser(sockets, nodes, threads, arch)


if __name__ == "__main__":
    main()
