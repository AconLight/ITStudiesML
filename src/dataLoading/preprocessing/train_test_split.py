import math
import random


class TrainTestSplitter():
    @staticmethod
    def split(dataset, test_set_percentage):
        if test_set_percentage is None:
            # TODO
            # dataset.splited_data
            return
        data_columns = dataset.get_data_columns()
        target_columns = dataset.get_target_columns()

        if(len(data_columns) == 0):
            raise ValueError("There are not data columns specified")
        if (len(target_columns) == 0):
            raise ValueError("There are not target columns specified")

        X = dataset.get_columns(dataset.get_data_columns())
        Y = dataset.get_columns(dataset.get_target_columns())

        number_of_examples = X.shape[0]
        train_set_size = number_of_examples - math.ceil(number_of_examples * test_set_percentage)

        training_set_indecies = random.sample(list(range(number_of_examples)),train_set_size)
        test_set_indecies = set(range(number_of_examples)).difference(training_set_indecies)

        X_train = X[X.index.isin(training_set_indecies)]
        Y_train = Y[Y.index.isin(training_set_indecies)]
        X_test = X[X.index.isin(test_set_indecies)]
        Y_test = Y[Y.index.isin(test_set_indecies)]

        return X_train, Y_train, X_test, Y_test

