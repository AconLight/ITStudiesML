from sklearn.metrics import accuracy_score


class AccuracyMetric:

    @staticmethod
    def calculate(y_prediction, data_map):
        return accuracy_score(data_map['CLASSIFICATION_COLUMN_test'], y_prediction)
