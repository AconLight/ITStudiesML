from src.serialization_flow.preprocess_algorithms.PreprocessAlgorithmBase import PreprocessAlgorithmBase


class LogScale(PreprocessAlgorithmBase):

    def __init__(self):
        self.params_possibilities = {
            "a": [1, 2, 3],
            "b": [4, 5, 6]
        }
        self.name = 'log scale'

    def preprocess(self, data, y, params):
        print('run ZScore with params:')
        print(params)
        return data