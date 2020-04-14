from src.modelProcessing.modelAlgorithms.algorithmBaseGroup import AlgorithmBaseGroup
import numpy as np

class DummyAlgorithmGroup(AlgorithmBaseGroup):
    def __init__(self, conf):
        super().__init__(conf)
        print("DummyAlgorithm initialized")

    def train(self):
        print("DummyAlgorithm train")

    def predict(self):
        print("DummyAlgorithm predict")
        return np.array(np.random.randn(self.X.shape[0],1)*10, dtype=np.int32)