import re
import csv
import os
import pandas as pd


def get_csv(name):
    file = open(name, 'r')
    return file


def numatest_parser():
    cwd = os.path.dirname(os.getcwd())
    sizes = ['62.5', '125', '250', '500']
    sizes_dic = {'62.5': '0.5', '125': '1', '250': '2', '500': '5'}
    threads_set = [8, 16, 32, 48, 64]
    for threads in threads_set:
        for size in sizes:
            route = '{}/outputs/numatest/'.format(cwd)
            with open(route + '{}_{}.csv'.format(threads, sizes_dic[size]), 'w') as csvfile:
                results_writer = csv.writer(csvfile, dialect='excel')
                #results_writer.writerow(['sep=,'])
                #results_writer.writerow(['bw', 'cores'])
                cores = [str(x) for x in range(0, threads)]
                results_writer.writerow(cores)

                for rep in range(1, 6):
                    results_per_rep = list()
                    results_per_rep.append(rep)
                    name = '{}/outputs/numatest/all_contention_argv.{}.{}.{}.txt'.format(cwd, size, threads, rep)
                    file = get_csv(name)
                    for line in file:
                        if re.search('all-contention', line):
                            line_bw = line.replace('\n', '')
                            line_bw = line_bw.split(' ')
                            line_bw = [x for x in line_bw if x != '']
                            print("Line found: ", line_bw)

                            results_per_rep.append(line_bw[8])
                    print("selected line", results_per_rep)
                    results_writer.writerow(results_per_rep)


def average_calc():
    cwd = os.path.dirname(os.getcwd())
    sizes = ['0.5', '1', '2', '5']
    threads_set = [8, 16, 32, 48, 64]
    for threads in threads_set:
        route = '{}/outputs/numatest/'.format(cwd)
        with open(route + '{}_processed.csv'.format(threads), 'w') as csvfile:
            results_writer = csv.writer(csvfile, dialect='excel')
            cores = ['size']
            for x in range(0, threads):
                cores.append(str(x))
            results_writer.writerow(cores)
            for size in sizes:
                line = list()
                name = '{}/outputs/numatest/{}_{}.csv'.format(cwd, threads, size)
                df = pd.read_csv(name)
                line.append(size)
                average = df.mean(axis=0)
                for x in average:
                    line.append(x)

                results_writer.writerow(line)




def main():
    numatest_parser()
    average_calc()


if __name__ == "__main__":
    main()