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
    sizes = ['05', '1', '2', '5']
    modes = ['persocket', 'wide']
    threads_set = [8, 16, 32, 48, 64]

    for mode in modes:
        route = '{}/outputs/stream/batcat/regular/{}/'.format(cwd, mode)
        with open(route + '{}.csv'.format(mode), 'w') as csvfile:
            os.chdir(route)
            results_writer = csv.writer(csvfile, dialect='excel')
            results_writer.writerow(['Name', 8, 16, 32, 48, 64])
            for size in sizes:
                average = [size]
                for threads in threads_set:
                    name = '{}.{}.{}.txt'.format(threads, size, mode)
                    name_file = find(name, route)
                    if name_file is not None:
                        exist_file = True
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
                                #print("Line found: ", line_exec_time)
                                # results_writer.writerow(line_exec_time)
                        print('matrix \n', matrix_file)
                        mean = np.mean([float(matrix_file[0][1]), float(matrix_file[1][1]), float(matrix_file[2][1]), float(matrix_file[3][1])])
                        average.append(mean)
                    else:
                        exist_file = False
                if exist_file:
                    print('row: {} size: {}'.format(average, len(average)))
                    results_writer.writerow(average)





def main():
    stream_parser()


if __name__ == "__main__":
    main()