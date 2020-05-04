from sklearn.metrics import recall_score


class RecallMetric:

    @staticmethod
    def calculate(y_prediction, data_map):
        return recall_score(data_map['FEED_COLUMNS'], y_prediction)
