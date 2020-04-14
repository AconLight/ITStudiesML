from sklearn.neighbors import KNeighborsClassifier

from src.modelProcessing.modelAlgorithms.algorithmBase import AlgorithmBase


class KNN(AlgorithmBase):
    def __init__(self, conf):
        super().__init__(conf)
        algorithm = (conf.get_entry('algorithm'))  # {‘auto’, ‘ball_tree’, ‘kd_tree’, ‘brute’}
        n_neighbors = int(conf.get_entry('n_neighbors'))

        self.classifier = KNeighborsClassifier(algorithm=algorithm, n_neighbors=n_neighbors)

    def train(self):
        self.classifier.fit(self.X_train, self.Y_train)

    def predict(self):
        return self.classifier.predict(self.X_test)
