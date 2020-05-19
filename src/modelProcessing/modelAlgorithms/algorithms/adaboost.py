import numpy as np
from sklearn.ensemble import AdaBoostClassifier
from src.modelProcessing.modelAlgorithms.algorithmBaseClassification import AlgorithmBase


class AdaBoost(AlgorithmBase):
    def __init__(self, conf):
        super().__init__(conf)
        n_estimators = int(conf.get_entry('n_estimators'))
        learning_rate = float(conf.get_entry('learning_rate'))

        self.model_algorithm = AdaBoostClassifier(n_estimators=n_estimators, learning_rate=learning_rate)

    def train(self):
        self.model_algorithm.fit(self.X_train, self.Y_train)

    def predict(self):
        return self.model_algorithm.predict(self.X_test)

# self.score(X, Y, [sample_weight]) - zwraca accuaracy