from sklearn.metrics import recall_score


class RecallMetric:

    @staticmethod
    def calculate(y_prediction, data_map):
        return recall_score(data_map["CLASSIFICATION_COLUMN_test"], y_prediction)
