from sklearn.metrics import accuracy_score


class DummyGroupMetric:

    @staticmethod
    def calculate(y_prediction, data_map):
        return 1
