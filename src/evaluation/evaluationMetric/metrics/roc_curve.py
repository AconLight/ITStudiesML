from sklearn.metrics import roc_curve


class RocCurve:

    @staticmethod
    def calculate(y_prediction, data_map):
        return roc_curve(data_map["CLASSIFICATION_COLUMN_test"], y_prediction)
