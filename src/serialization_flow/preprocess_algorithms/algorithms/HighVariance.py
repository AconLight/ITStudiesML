from src.serialization_flow.preprocess_algorithms.PreprocessAlgorithmBase import PreprocessAlgorithmBase
import numpy as np
import pandas as pd

class HighVaraince(PreprocessAlgorithmBase):

    def __init__(self):
        self.params_possibilities = {
            "columns_to_reduce": [1, 2, 3],
        }
        self.name = 'High Variance'

    def preprocess(self, data, params):
        variances = []
        data_by_col = []
        cols = []
        for column in data:
            variances.append(np.var(data[column].values))
            data_by_col.append(data[column])
            cols.append(column)

        column_size = len(cols)
        idxs = []
        for col in range(column_size - params['columns_to_reduce']):
            idxs.append(np.argmax(variances))
            variances.remove(variances[idxs[col]])

        npdf = pd.DataFrame(columns=list(map(str, range(column_size - params['columns_to_reduce']))))
        for col in range(column_size - params['columns_to_reduce']):
            npdf[cols[idxs[col]]] = data_by_col[idxs[col]]
        return npdf