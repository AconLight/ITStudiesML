class AlgorithmBase:
    def __init__(self, conf):
        pass

    def setup(self, data_map):
        self.data_map = data_map
        self.Y_train = self.data_map["FEED_COLUMNS"]
        print(self.Y_train)
        self.Y_train = self.data_map["Y_train"].values.ravel()
        self.X_train = self.data_map["X_train"]
        self.Y_test = self.data_map["Y_test"]
        self.X_test = self.data_map["X_test"]

    def train(self):
        pass

    def predict(self):
        pass