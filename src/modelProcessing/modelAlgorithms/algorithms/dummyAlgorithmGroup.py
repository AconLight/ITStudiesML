from src.modelProcessing.modelAlgorithms.algorithmBaseGroup import AlgorithmBaseGroup


class DummyAlgorithmGroup(AlgorithmBaseGroup):
    def __init__(self, conf):
        super().__init__(conf)
        print("DummyAlgorithm initialized")

    def train(self):
        print("DummyAlgorithm train")

    def predict(self):
        print("DummyAlgorithm predict")
        return self.X