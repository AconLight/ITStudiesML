from sklearn.metrics import accuracy_score


class AccuracyMetric:

    @staticmethod
    def calculate(y_prediction, data_map):
        return accuracy_score(data_map['FEED_COLUMNS'], y_prediction)
