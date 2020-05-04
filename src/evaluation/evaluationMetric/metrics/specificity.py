from sklearn.metrics import f1_score
import numpy as np

class SpecificityMetric:

    @staticmethod
    def calculate(y_prediction, data_map):
        # print(data_map['CLASSIFICATION_COLUMN_test'].values.flatten())
        # print(y_prediction.values.flatten())
        score = f1_score(data_map['CLASSIFICATION_COLUMN_test'].values.flatten(), y_prediction.values.flatten(), average=None, zero_division=0)
        # print('specifity:', score)
        return np.average(score)