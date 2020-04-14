from pandas import DataFrame

from src.modelProcessing.modelAlgorithms.algorithmBaseClassification import AlgorithmBase


class DummyAlgorithm(AlgorithmBase):
    def __init__(self, conf):
        super().__init__(conf)
        print("DummyAlgorithm initialized")

    def train(self):
        print("DummyAlgorithm train")

    def predict(self):
        print("DummyAlgorithm predict")
        return self.Y_train[:self.X_test.shape[0]]