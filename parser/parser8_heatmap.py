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

    for mode in modes:
        for size in sizes:
            route = '{}/outputs/stream/{}/{}/{}/'.format(cwd, arch, threads, size)
            with open(route + '{}_heatmap_wcorrected.csv'.format(mode), 'w') as csvfile:
                os.chdir(route)
                results_writer = csv.writer(csvfile, dialect='excel')
                results_writer.writerow(['processor', 'node', 'bw'])
                for socket in range(0, int(sockets)):
                    for node in range(0, int(nodes)):
                        # stream_membind_batman_1GB_proc0_mem0_8t_sense_1936
                        name = 'stream_membind_{}_{}GB_proc{}_mem{}_{}t_{}*'.format(arch, size, socket, node, threads,
                                                                                    mode)
                        average = [socket]
                        average.append(node)
                        name_file = find(name, route)
                        if name_file is not None:
                            print('Opening ', name_file)
                            file = open(route + name_file, 'r')
                            matrix_file = list()
                            for line in file:
                                if re.search('Copy', line) or re.search('Scale', line) or re.search('Add', line) \
                                        or re.search('Triad', line):
                                    line_exec_time = line.replace('\n', '')
                                    line_exec_time = line_exec_time.split(' ')
                                    line_exec_time = [x for x in line_exec_time if x != '']
                                    matrix_file.append(line_exec_time)
                                    print("Line found: ", line_exec_time)
                                    # results_writer.writerow(line_exec_time)

                            mean = np.mean(
                                [float(matrix_file[0][1]), float(matrix_file[1][1]), float(matrix_file[2][1]),
                                 float(matrix_file[3][1])])
                            average.append(mean)
                            results_writer.writerow(average)


def main():
    # print("Welcome to results parser")
    # sockets = input("How many sockets? ")
    # nodes = input("How many memory nodes? ")
    threads = input("How many threads? ")
    arch = 'batcat'
    if arch == 'penguin':
        sockets = nodes = 4
    else:
        sockets = nodes = 8

    stream_parser(sockets, nodes, threads, arch)


if __name__ == "__main__":
    main()
