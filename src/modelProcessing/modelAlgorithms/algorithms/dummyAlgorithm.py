from pandas import DataFrame

from src.modelProcessing.modelAlgorithms.algorithmBaseClassification import AlgorithmBase


class DummyAlgorithm(AlgorithmBase):
    def __init__(self, conf):
        super().__init__(conf)

    def train(self):
        pass

    def predict(self):
        return self.Y_train[:self.X_test.shape[0]]