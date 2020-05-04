from sklearn.metrics import accuracy_score


class AccuracyMetric:

    @staticmethod
    def calculate(y_prediction, data_map):
        # print(data_map['CLASSIFICATION_COLUMN_test'].values.flatten())
        # print(y_prediction.values.flatten())
        score = accuracy_score(data_map['CLASSIFICATION_COLUMN_test'].values.flatten(), y_prediction.values.flatten())
        # print('accuracy:', score)
        return score