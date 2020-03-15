from scipy.stats import norm
import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB


class NaiveBayes():
    def __init__(self, conf) -> None:
        super().__init__()
        self.classifier = GaussianNB()

    def train(self,X_train, Y_train):
        self.classifier.fit(X_train,Y_train)

    def predict(self,X_test):
        return self.classifier.predict(X_test)


