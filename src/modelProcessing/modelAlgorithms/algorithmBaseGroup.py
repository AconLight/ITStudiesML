class AlgorithmBaseGroup:
    def __init__(self, conf):
        pass

    def setup(self, data_map):
        self.data_map = data_map
        self.X = self.data_map["FEED_COLUMNS"]

    def train(self):
        pass

    def predict(self):
        pass