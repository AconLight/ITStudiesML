from sklearn.metrics import recall_score, confusion_matrix
import numpy as np

class RecallMetric:

    @staticmethod
    def calculate(y_prediction, data_map):
        # print(data_map['CLASSIFICATION_COLUMN_test'].values.flatten())
        # print(y_prediction.values.flatten())
        score = recall_score(data_map['CLASSIFICATION_COLUMN_test'].values.flatten(), y_prediction.values.flatten(), average=None, zero_division=0)
        # print('recall:', score)
        return np.average(score)
