import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def get_csv(route, name):
    # df = pd.read_csv(route + mode + '.csv', index_col=0)
    # df = pd.pivot_table(route + mode, index='socket', values='bw', columns='node')
    print(route + name)
    df = sns.load_dataset(name, data_home=route)
    df = df.pivot("processor", "node", "bw")
    # print(df.head())
    return df


def reorder_csv(csv_list):
    csv_list.pop(0)
    # print(csv_list)
    for x in csv_list:
        x.pop(0)
    return csv_list


def generate_heatmap(csv_list, route, size, mode, threads, experiment, arch):
    square_value = True
    angle = 0
    value_max = 16000
    value_min = 2000
    plot_size = 15
    if threads == '8':
        if arch == 'batcat':
            value_max = 12000
        else:
            value_max = 16000

    if threads == '16':
        square_value = False
        value_max = 15000
        value_min = 3000

    if threads == '32':
        square_value = False
        if arch == 'batcat':
            plot_size = 20
        value_max = 15000
        value_min = 5000
        angle = 40

    sns.set(font_scale=2)
    plt.clf()
    plt.subplots(figsize=(plot_size, 15))
    g = sns.heatmap(csv_list, vmax=value_max, vmin=value_min, cmap="summer_r", xticklabels=True, square=square_value,
                    yticklabels=True, linewidths=0.1, cbar_kws={'label': 'bandwidth MB/s'})
    plt.title('Bandwidth {} threads vs 8 nodes - {} GB'.format(threads, size))
    # plt.title('Bandwidth {} threads vs 8 nodes -  {}'.format(threads, experiment))
    g.set_xticklabels(g.get_xticklabels(), fontsize=20)
    g.set_yticklabels(g.get_yticklabels(), rotation=angle, fontsize=14)

    # plt.savefig('{}/{}_{}_{}.png'.format(route, size, mode, experiment))

    # figure = g.get_figure()
    plt.savefig('{}/{}_{}_{}_WCORRECTED.png'.format(route, size, mode, experiment), dpi=400)


def main():
    sizes = ['05', '1', '2', '5']
    # sizes = ['05']
    modes = ['amb', 'sense']
    # modes = ['sense']
    # threads_set = ['8', '16']
    threads_set = ['32']
    experiments = ['membind', 'interleave']
    arch = 'batcat'

    cwd = os.path.dirname(os.getcwd())

    for threads in threads_set:
        for size in sizes:
            for mode in modes:
                route = '{}/outputs/stream/{}/{}/{}/'.format(cwd, arch, threads, size)
                if threads == '8':
                    name = mode + '_heatmap' + '_wcorrected'
                    # name = mode
                    csv_list = get_csv(route, name)
                    generate_heatmap(csv_list, route, size, mode, threads, '', arch)
                else:
                    for experiment in experiments:
                        name = mode + '_' + experiment + '_heatmap' + '_wcorrected'
                        # name = mode + '_' + experiment
                        csv_list = get_csv(route, name)
                        generate_heatmap(csv_list, route, size, mode, threads, experiment, arch)


if __name__ == "__main__":
    main()
