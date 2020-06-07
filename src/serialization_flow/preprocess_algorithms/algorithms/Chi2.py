from sklearn.feature_selection import SelectKBest, chi2

from src.serialization_flow.preprocess_algorithms.PreprocessAlgorithmBase import PreprocessAlgorithmBase
import numpy as np

class Chi2(PreprocessAlgorithmBase):

    def __init__(self):
        self.params_possibilities = {
            "columns_to_reduce": [0, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15],
        }
        self.name = 'chi2'

    def preprocess(self, data, y, params):
        size = len(list(data.head()))
        data2 = data.copy()
        for column in list(data2.head()):
            max_val = -np.min(data[column].values) + 1
            data2[column] = data2[column].apply(lambda x: x + max_val)

        selector = SelectKBest(score_func=chi2, k=size-params['columns_to_reduce'])
        selected = selector.fit_transform(data2, y)
        # Get columns to keep and create new dataframe with those only
        cols = selector.get_support(indices=True)
        columns = []
        for col in cols:
            columns.append(list(data.head())[col])
        print(params)
        print(columns)
        # params['selected_columns'] = str(columns)
        drop_cols = [x for x in list(data.head()) if x not in columns]
        return data.drop(drop_cols, axis=1)
