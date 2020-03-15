from sklearn.neighbors import KNeighborsClassifier


class KNN:
    def __init__(self) -> None:
        super().__init__()
        self.classifier = KNeighborsClassifier()

    def train(self, x_train, y_train):
        self.classifier.fit(x_train, y_train)

    def predict(self, x_test):
        return self.classifier.predict(x_test)
