from scipy.stats import norm
import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier


class MLP:
    def __init__(self) -> None:
        super().__init__()
        self.classifier = MLPClassifier(solver='adam', alpha=1e-6, hidden_layer_sizes=(20, 2))

    def train(self, x_train, y_train):
        self.classifier.fit(x_train, y_train)

    def predict(self, x_test):
        return self.classifier.predict(x_test)