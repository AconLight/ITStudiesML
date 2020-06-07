from itertools import product

from src.serialization_flow.preprocess_algorithms.algorithms.Chi2 import Chi2
from src.serialization_flow.preprocess_algorithms.algorithms.HighVariance import HighVariance
from src.serialization_flow.preprocess_algorithms.algorithms.LogScale import LogScale
from src.serialization_flow.preprocess_algorithms.algorithms.LowVariance import LowVariance
from src.serialization_flow.preprocess_algorithms.algorithms.MinMax import MinMax
from src.serialization_flow.preprocess_algorithms.algorithms.ZScore import ZScore


class DataPreprocessor():

    def setup1(self):
        # selekcja
        chi2 = Chi2()

        # normalizacja
        zscore = ZScore()
        log1 = LogScale()
        log1.params_possibilities = {"column_id": [8]}
        log2 = LogScale()
        log2.params_possibilities = {"column_id": [9]}
        log3 = LogScale()
        log3.params_possibilities = {"column_id": [10]}

        # self.data_preprocess_elements = [log1, log2, log3]
        self.data_preprocess_elements = []

    def __init__(self):
        self.setup1()


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
        my_data_preprocess_elements = [Chi2()]
        possibilities = []
        for data_preprocess_element in my_data_preprocess_elements:
            func_params_names = []
            for function in data_preprocess_element.get_all_params_possibilities():
                func_params_names.append(function)
            possibilities.append(func_params_names)

        possibilities_prod = list(product(*possibilities))
        return possibilities_prod

