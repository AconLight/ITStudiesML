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
    file_name += '.svg'
    return folder_path + file_name


def parameter_comparison_plot(algorithm_id, database_id, parameter_id, parameter_values):
    sns.set(style="darkgrid")

    df = pd.DataFrame([], columns=[parameter_id, 'value'])

    for index, key in enumerate(parameter_values):
        df.loc[index] = [key, parameter_values[key]]
    print(df)

    sns.lineplot(x=parameter_id, y="value", data=df)

    file_path = get_file_path([algorithm_id, database_id, parameter_id])
    plt.savefig(file_path, format='svg')


def algorithm_comparison_plot():
    # TODO implement similar to example above
    pass
