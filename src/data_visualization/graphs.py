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

    file_path = get_file_path([algorithm_id, database_id[5:-4], metric_id,  parameter_id])
    plt.savefig(file_path, format='png')
    plt.cla()
    plt.clf()


def algorithm_comparison_plot(database_id, metric_id, best_results):
    df = pd.DataFrame([], columns=['algorithms', metric_id])
    for index, best_result in enumerate(best_results):
        df.loc[index] = [best_result[0], best_result[1]]

    sns.scatterplot(x='algorithms', y=metric_id, data=df)

    file_path = get_file_path(['algorithms', database_id[5:-4], metric_id])
    plt.savefig(file_path, format='png')
    plt.cla()
    plt.clf()
    # TODO implement similar to example above
    pass
