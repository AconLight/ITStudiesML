from src.modelProcessing.modelAlgorithms.algorithmBaseGroup import AlgorithmBaseGroup


class DummyAlgorithmGroup(AlgorithmBaseGroup):
    def __init__(self, conf):
        super().__init__(conf)

    def train(self):
        pass

    def predict(self):
        return self.X