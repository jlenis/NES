
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def get_csv(route, mode):
    #df = pd.read_csv(route + mode + '.csv', index_col=0)
    #df = pd.pivot_table(route + mode, index='socket', values='bw', columns='node')
    print(route + mode)
    df = sns.load_dataset(mode, data_home=route)
    df = df.pivot("socket", "node", "bw")
    print(df.head())
    return df


def reorder_csv(csv_list):
    csv_list.pop(0)
    print(csv_list)
    for x in csv_list:
        x.pop(0)
    return csv_list


def generate_heatmap(csv_list, route, size, mode):
    sns.set()
    g = sns.heatmap(csv_list, cmap="summer_r")
    plt.title('Bandwidth 8 sockets vs 8 nodes')
    plt.show()
    figure = g.get_figure()
    figure.savefig('{}/{}_{}.png'.format(route, size, mode))

def main():
    sizes = ['05', '1', '2', '5']
    modes = ['amb', 'sense']
    threads_set = [32]

    cwd = os.path.dirname(os.getcwd())

    for threads in threads_set:
        for size in sizes:
            for mode in modes:
                route = '{}/outputs/stream/batcat/{}/{}/new/'.format(cwd, threads, size)
                csv_list = get_csv(route, mode)
                generate_heatmap(csv_list, route, size, mode)
                input()


if __name__ == "__main__":
    main()
