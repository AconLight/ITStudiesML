from sklearn.neural_network import MLPClassifier

import numpy as np
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit

from src.modelProcessing.modelAlgorithms.algorithmBaseClassification import AlgorithmBase


class MLP(AlgorithmBase):
    def __init__(self, conf):
        super().__init__(conf)
        alpha = float(conf.get_entry('alpha'))
        hidden_layer_count = int(conf.get_entry('hidden_layer_count'))
        hidden_layer_neurons = int(conf.get_entry('hidden_layer_neurons'))
        hidden_layer_sizes = (hidden_layer_neurons, hidden_layer_count)
        solver = conf.get_entry('solver')
        self.model_algorithm = MLPClassifier(alpha=alpha, hidden_layer_sizes=hidden_layer_sizes, solver=solver)

    def train(self):
        self.model_algorithm.fit(self.X_train, self.Y_train)
        self.learning_data = learning_curve(self.model_algorithm, self.X_train, self.Y_train,
                                            cv=ShuffleSplit(n_splits=100, test_size=0.2, random_state=0), n_jobs=4,
                                            train_sizes=np.linspace(.1, 1.0, 5),
                                            return_times=True)

    def predict(self):
        return self.model_algorithm.predict(self.X_test)
