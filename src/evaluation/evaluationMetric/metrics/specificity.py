from sklearn.metrics import f1_score


class SpecificityMetric:

    @staticmethod
    def calculate(y_prediction, data_map):
        return f1_score(data_map['FEED_COLUMNS'], y_prediction)
