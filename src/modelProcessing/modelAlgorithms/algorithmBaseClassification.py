class AlgorithmBase:
    def __init__(self, conf):
        self.model_algorithm = None

    def setup(self, data_map):
        self.data_map = data_map
        self.Y_train = self.data_map["CLASSIFICATION_COLUMN_train"].values.ravel()
        self.X_train = self.data_map["FEED_COLUMNS_train"]

        self.Y_test = self.data_map["CLASSIFICATION_COLUMN_test"]
        self.X_test = self.data_map["FEED_COLUMNS_test"]

        self.learning_data = None

    def train(self):
        pass

    def predict(self):
        pass