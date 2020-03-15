from sklearn.ensemble import RandomForestClassifier


class RandomForest:
    def __init__(self, conf) -> None:
        super().__init__()
        self.classifier = RandomForestClassifier()

    def train(self, x_train, y_train):
        self.classifier.fit(x_train, y_train)

    def predict(self, x_test):
        return self.classifier.predict(x_test)
