from sklearn.metrics import recall_score, confusion_matrix


class RecallMetric:

    @staticmethod
    def calculate(y_prediction, data_map):
        # print(data_map['CLASSIFICATION_COLUMN_test'].values.flatten())
        # print(y_prediction.values.flatten())
        score = recall_score(data_map['CLASSIFICATION_COLUMN_test'].values.flatten(), y_prediction.values.flatten(), average='weighted')
        # print('recall:', score)
        return score
