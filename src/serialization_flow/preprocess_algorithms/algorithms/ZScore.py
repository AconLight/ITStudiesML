from src.serialization_flow.preprocess_algorithms.PreprocessAlgorithmBase import PreprocessAlgorithmBase
import numpy as np

class ZScore(PreprocessAlgorithmBase):

    def __init__(self, u=None, q=None):
        self.u = u
        self.q = q
        self.params_possibilities = {
            "column_id": [0, 1],
        }
        self.name = 'z-score'

    def preprocess(self, data, y, params):
        column = list(data.head())[int(params["column_id"])]
        if self.u is None:
            my_u = np.mean(data[column].values)
            my_q = np.std(data[column].values)
        else :
            my_u = self.u
            my_q = self.q

        params['used_q'] = my_q
        params['used_u'] = my_u

        print('run ZScore with params:')
        print(params)
        data[column] = data[column].apply(lambda x: (x-my_u)/my_q)
        return data