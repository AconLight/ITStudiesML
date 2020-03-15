from sklearn.neighbors import KNeighborsClassifier


class KNN:
    def __init__(self, conf) -> None:
        super().__init__()
        algorithm = (conf.get_entry('algorithm'))  # {‘auto’, ‘ball_tree’, ‘kd_tree’, ‘brute’}
        n_neighbors = int(conf.get_entry('n_neighbors'))

        self.classifier = KNeighborsClassifier(algorithm=algorithm, n_neighbors=n_neighbors)

    def train(self, x_train, y_train):
        self.classifier.fit(x_train, y_train)

    def predict(self, x_test):
        return self.classifier.predict(x_test)
