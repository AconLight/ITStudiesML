from sklearn.metrics import precision_score


class PrecisionMetric:

    @staticmethod
    def calculate(y_prediction, data_map):
        return precision_score(data_map["CLASSIFICATION_COLUMN_test"], y_prediction)
