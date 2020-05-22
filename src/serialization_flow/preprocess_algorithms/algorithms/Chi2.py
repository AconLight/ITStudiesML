from sklearn.feature_selection import SelectKBest, chi2

from src.serialization_flow.preprocess_algorithms.PreprocessAlgorithmBase import PreprocessAlgorithmBase


class Chi2(PreprocessAlgorithmBase):

    def __init__(self):
        self.params_possibilities = {
            "columns_to_reduce": [1, 2, 3],
        }
        self.name = 'chi2'

    def preprocess(self, data, y, params):
        size = len(list(data.columns))
        return SelectKBest(score_func=chi2, k=size-params['columns_to_reduce']).fit_transform(data, y)
