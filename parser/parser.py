import re
import csv
import numpy as np
import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def stream_parser(sockets, nodes, threads, job_id):
    # # cwd = os.getcwd()
    cwd = os.path.dirname(os.getcwd())
    machines = ['catwoman', 'batman']
    sizes = ['05', '1', '2', '5']
    modes = ['amb', 'sense']
    for x in range(job_id, job_id + 8):
        for mode in modes:
            for size in sizes:
                for machine in machines:
                    route = '{}/outputs/stream/batcat/{}/{}/'.format(cwd, threads, size)
                    with open(route + '{}_{}_{}.csv'.format(mode, size, job_id), 'w') as csvfile:
                        os.chdir(route)
                        results_writer = csv.writer(csvfile, dialect='excel')
                        results_writer.writerow(['Sockets\Mem_Nodes', 0, 1, 2, 3, 4, 5, 6, 7])
                        for socket in range(0, int(sockets)):
                            average = [socket]
                            for node in range(0, int(nodes)):

                                #stream_membind_batman_1GB_proc0_mem0_8t_sense_1936
                                name = 'stream_membind_{}_{}GB_proc{}_mem{}_{}t_{}_{}.txt'.format(machine, size, socket,
                                                                                                node, threads, mode,  x)
                                #print('Directory: {} - File Name: {}'.format(route, name))
                                if os.path.isfile(name):
                                    print('Opening ', name)
                                    file = open(route + name, 'r')
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

                                    mean = np.mean([float(matrix_file[0][1]), float(matrix_file[1][1]), float(matrix_file[2][1]), float(matrix_file[3][1])])
                                    average.append(mean)
                            print('row', average)
                            results_writer.writerow(average)



def main():
    # print("Welcome to results parser")
    # sockets = input("How many sockets? ")
    # nodes = input("How many memory nodes? ")
    threads = input("How many threads? ")
    sockets = nodes = 8
    job_id = int(input("Starting jobID? "))
    stream_parser(sockets, nodes, threads, job_id)


if __name__ == "__main__":
    main()