import math
import random


class TrainTestSplitter():
    @staticmethod
    def split(dataset, test_set_percentage, preprocess_functions):
        data_map = {}
        training_set_indecies = None
        test_set_indecies = None
        print('dataset.splited_data')
        print(dataset.splited_data)
        for columns_key in dataset.splited_data.keys():
            columns = dataset.splited_data[columns_key]
            if len(columns) == 0:
                raise ValueError("There are not data columns specified")
            if len(columns_key.split('FEED')) > 1:
                data = dataset.get_columns(columns)
                for function in preprocess_functions:
                    data = function['func'](data)
            else:
                data = dataset.get_columns(columns)
            if test_set_percentage == 0:
                data_map[columns_key] = data
            else:
                number_of_examples = data.shape[0]
                train_set_size = number_of_examples - math.ceil(number_of_examples * test_set_percentage)
                if training_set_indecies is None:
                    training_set_indecies = random.sample(list(range(number_of_examples)),train_set_size)
                    test_set_indecies = set(range(number_of_examples)).difference(training_set_indecies)
                data_map[str(columns_key)+"_train"] = data[data.index.isin(training_set_indecies)]
                data_map[str(columns_key)+"_test"] = data[data.index.isin(test_set_indecies)]

        return data_map
