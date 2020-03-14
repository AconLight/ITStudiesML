from pandas import DataFrame


class DummyAlgorithm:
    def __init__(self):
        print("DummyAlgorithm initialized")

    def train(self, X_train, Y_train):
        self.Y_train = Y_train
        print("DummyAlgorithm train")

    def predict(self, X_test):
        print("DummyAlgorithm predict")
        return self.Y_train[:X_test.shape[0]]