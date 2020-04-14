import importlib

from pandas import DataFrame


class ModelProcessor:
    def __init__(self, configuration, file):
        self.file = file
        self.configuration = configuration
        self.model = getattr(importlib.import_module("src.modelProcessing.modelAlgorithms.algorithms"), configuration.get_entry('modelAlgorithm'))(configuration)

    def process(self, data_map):
        self.model.setup(data_map)
        self.file.write("model algorithm: " + str(self.configuration.get_entry('modelAlgorithm')) + '\n')
        self.model.train()
        return DataFrame(self.model.predict(), columns=None)


