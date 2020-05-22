from itertools import product

from src.serialization_flow.preprocess_algorithms.algorithms.Chi2 import Chi2
from src.serialization_flow.preprocess_algorithms.algorithms.ZScore import ZScore


class DataPreprocessor():

    def __init__(self):
        self.data_preprocess_elements = [ZScore()]

    def load(self):
        pass

    def save(self):
        pass

    def preprocess(self, data):
        for data_preprocess_element in self.data_preprocess_elements:
            pass
            # data = data_preprocess_element(data)

        return data

    def get_all_possibilities(self):
        possibilities = []
        for data_preprocess_element in self.data_preprocess_elements:
            func_params_names = []
            for function in data_preprocess_element.get_all_params_possibilities():
                func_params_names.append(function)
            possibilities.append(func_params_names)

        possibilities_prod = list(product(*possibilities))
        return possibilities_prod

    def get_single_possibility(self):
        zscore = ZScore()
        zscore.params_possibilities = {
            "a": [1],
            "b": [2]
        }
        my_data_preprocess_elements = [zscore]
        possibilities = []
        for data_preprocess_element in my_data_preprocess_elements:
            func_params_names = []
            for function in data_preprocess_element.get_all_params_possibilities():
                func_params_names.append(function)
            possibilities.append(func_params_names)

        possibilities_prod = list(product(*possibilities))
        return possibilities_prod

