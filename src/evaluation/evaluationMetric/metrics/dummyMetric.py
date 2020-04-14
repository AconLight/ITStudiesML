

class DummyMetric:
    def __init__(self):
        pass

    def calculate(self, pd_Y_pred, pd_Y_test):
        return "dummy results"