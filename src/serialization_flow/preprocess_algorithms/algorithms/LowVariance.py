from src.serialization_flow.preprocess_algorithms.PreprocessAlgorithmBase import PreprocessAlgorithmBase


class ZScore(PreprocessAlgorithmBase):

    def __init__(self):
        self.params_possibilities = {
            "a": [1, 2, 3],
            "b": [4, 5, 6]
        }
        self.name = 'z-score'

    def preprocess(self, data, params):
        print('run ZScore with params:')
        print(params)
        return data