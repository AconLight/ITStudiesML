from src.modelProcessing.modelAlgorithms.algorithmBaseGroup import AlgorithmBaseGroup
import numpy as np

class DummyAlgorithmGroup(AlgorithmBaseGroup):
    def __init__(self, conf):
        super().__init__(conf)

    def train(self):
        pass

    def predict(self):
        return np.array(np.random.randn(self.X.shape[0],1)*10, dtype=np.int32)
