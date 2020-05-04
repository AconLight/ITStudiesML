from sklearn.metrics import accuracy_score


class AccuracyMetric:

    @staticmethod
    def calculate(y_prediction, data_map):
        print("dupa")
        print(data_map['CLASSIFICATION_COLUMN_test'])
        print(y_prediction)
        return accuracy_score(data_map['CLASSIFICATION_COLUMN_test'], y_prediction)
