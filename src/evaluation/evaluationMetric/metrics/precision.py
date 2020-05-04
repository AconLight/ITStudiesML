from sklearn.metrics import precision_score


class PrecisionMetric:

    @staticmethod
    def calculate(y_prediction, data_map):
        # print(data_map['CLASSIFICATION_COLUMN_test'].values.flatten())
        # print(y_prediction.values.flatten())
        score = precision_score(data_map['CLASSIFICATION_COLUMN_test'].values.flatten(), y_prediction.values.flatten(), average='micro')
        # print('precision:', score)
        return score
