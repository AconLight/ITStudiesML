from sklearn.metrics import precision_score


class PrecisionMetric:

    @staticmethod
    def calculate(y_prediction, data_map):
        return precision_score(data_map['FEED_COLUMNS'], y_prediction)
