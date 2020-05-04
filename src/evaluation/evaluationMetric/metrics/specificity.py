from sklearn.metrics import f1_score


class SpecificityMetric:

    @staticmethod
    def calculate(y_prediction, data_map):
        # print(data_map['CLASSIFICATION_COLUMN_test'].values.flatten())
        # print(y_prediction.values.flatten())
        score = f1_score(data_map['CLASSIFICATION_COLUMN_test'].values.flatten(), y_prediction.values.flatten(), average='micro')
        # print('specifity:', score)
        return score