from src.serialization_flow.preprocess_algorithms.PreprocessAlgorithmBase import PreprocessAlgorithmBase
import numpy as np

class LogScale(PreprocessAlgorithmBase):

    def __init__(self):
        self.params_possibilities = {
            "column_id": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        }
        self.name = 'log scale'

    def preprocess(self, data, y, params):
        print('run LogScale with params:')
        print(params)
        column = list(data.head())[int(params["column_id"])]
        print(column)
        max_val = -np.min(data[column].values) + 1
        data[column] = data[column].apply(lambda x: np.log(x + max_val))
        return data