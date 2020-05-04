from sklearn.metrics import f1_score


class SpecificityMetric:

    @staticmethod
    def calculate(y_prediction, data_map):
        return f1_score(data_map['CLASSIFICATION_COLUMN_test'], y_prediction, average='micro')
