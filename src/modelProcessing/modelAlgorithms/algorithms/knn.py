from sklearn.neighbors import KNeighborsClassifier

import numpy as np
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit

from src.modelProcessing.modelAlgorithms.algorithmBaseClassification import AlgorithmBase


class KNN(AlgorithmBase):
    def __init__(self, conf):
        super().__init__(conf)
        algorithm = (conf.get_entry('algorithm'))  # {‘auto’, ‘ball_tree’, ‘kd_tree’, ‘brute’}
        n_neighbors = int(conf.get_entry('n_neighbors'))

        self.classifier = KNeighborsClassifier(algorithm=algorithm, n_neighbors=n_neighbors)

    def train(self):
        self.classifier.fit(self.X_train, self.Y_train)
        self.learning_data = learning_curve(self.classifier, self.X_train, self.Y_train,
                                            cv=ShuffleSplit(n_splits=100, test_size=0.2, random_state=0), n_jobs=4,
                                            train_sizes=np.linspace(.1, 1.0, 5),
                                            return_times=True)

    def predict(self):
        return self.classifier.predict(self.X_test)
