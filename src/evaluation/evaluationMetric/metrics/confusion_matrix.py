from sklearn.metrics import confusion_matrix


class ConfusionMatrix:

    @staticmethod
    def calculate(y_prediction, data_map):
        return confusion_matrix(data_map["CLASSIFICATION_COLUMN_test"], y_prediction)
