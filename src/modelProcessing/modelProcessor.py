import importlib

class ModelProcessor:
    def __init__(self, configuration):
        self.model = getattr(importlib.import_module("src.modelProcessing.modelAlgorithms.algorithms"), configuration.get_entry('modelAlgorithm'))()

    def process(self, X_train, X_test, Y_train):
        self.model.train(X_train, Y_train)
        return self.model.predict(X_test)


