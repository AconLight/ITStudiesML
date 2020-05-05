import importlib

from pandas import DataFrame

from src.data_visualization.effectiveness import plot_learning_curve


class ModelProcessor:
    def __init__(self, configuration, file):
        self.file = file
        self.configuration = configuration
        self.model = getattr(importlib.import_module("src.modelProcessing.modelAlgorithms.algorithms"), configuration.get_entry('modelAlgorithm'))(configuration)

    def process(self, data_map):
        self.model.setup(data_map)
        self.file.write("model algorithm: " + str(self.configuration.get_entry('modelAlgorithm')) + '\n')
        self.model.train()
        if self.model.learning_data is not None:
            plot_learning_curve(self.model.self.learning_data)
        return DataFrame(self.model.predict(), columns=None)


