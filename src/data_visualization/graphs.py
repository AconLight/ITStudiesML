import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pathlib
from os import sep


def get_file_path(file_name_ids):
    folder_path = str(pathlib.Path(__file__).parent.absolute().parent.parent) + sep + 'generated_graphs' + sep
    file_name = ''
    for file_name_id in file_name_ids:
        file_name += file_name_id
        file_name += '_'
    file_name = file_name[:-1]
    file_name += '.png'
    return folder_path + file_name


def parameter_comparison_plot(algorithm_id, database_id, metric_id, parameter_id, parameter_values):
    df = pd.DataFrame([], columns=[parameter_id, metric_id])
    for index, parameter_value in enumerate(parameter_values):
        df.loc[index] = [parameter_value['param_val'], parameter_value['metric_val']]

    sns.scatterplot(x=parameter_id, y=metric_id, data=df)

    file_path = get_file_path([algorithm_id, database_id[5:-4], metric_id, parameter_id])
    plt.savefig(file_path, format='png')
    plt.cla()
    plt.clf()


def groups_dist_plot(algorithm_id, database_id, metric_id, parameter_id, parameter_values):
    # for columns
    for index, parameter_value in enumerate(parameter_values):
        print(parameter_value['data'])
        print(parameter_value['process_result'])


def algorithm_comparison_plot(database_id, metric_id, best_results):
    df = pd.DataFrame([], columns=['algorithms', metric_id])
    for index, best_result in enumerate(best_results):
        df.loc[index] = [best_result[0], best_result[1]]

    sns.scatterplot(x='algorithms', y=metric_id, data=df)

    file_path = get_file_path(['algorithms', database_id[5:-4], metric_id])
    plt.savefig(file_path, format='png')
    plt.cla()
    plt.clf()
    pass


def parameter_plot(database_id, metric_id, algorithm_id, parameter_id, column_1_id, column_2_id, data, results):
    df = pd.DataFrame([], columns=[column_1_id, column_2_id, 'classes'])
    for index, result in enumerate(results):
        df.loc[index] = [data[column_1_id][index], data[column_2_id][index], result]

    sns.scatterplot(x=column_1_id, y=column_2_id, hue='classes', data=df)

    file_path = get_file_path(
        ['classes', database_id[5:-4], metric_id, algorithm_id, parameter_id, column_1_id, column_2_id])
    plt.title("Plot {} {} {} {}".format(database_id[5:-4], metric_id, algorithm_id, parameter_id))
    plt.savefig(file_path, format='png')
    plt.cla()
    plt.clf()
    pass
