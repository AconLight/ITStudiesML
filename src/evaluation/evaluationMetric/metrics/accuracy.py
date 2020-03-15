from sklearn.metrics import accuracy_score


class AccuracyMetric:

    @staticmethod
    def calculate(y_prediction, y_true):
        return accuracy_score(y_true, y_prediction)
