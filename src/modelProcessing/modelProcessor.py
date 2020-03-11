import importlib

from src.common.classificationOutput import ClassificationOutput


class ModelProcessor:
    def __init__(self, conf):
        self.model = getattr(importlib.import_module("src.modelProcessing.modelAlgorithms.algorithms"), conf['modelAlgorithm'])()

    def process(self, X_train, X_test, Y_train, Y_test):
        self.model.train(X_train, Y_train)
        Y_pred = self.model.predict(X_test)

        return ClassificationOutput(Y_test, Y_pred)


