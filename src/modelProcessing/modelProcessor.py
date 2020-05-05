import importlib

from pandas import DataFrame

from src.common.configuration.conf import DataLoadingConfigurationEntries
from src.data_visualization.effectiveness import plot_learning_curve


class ModelProcessor:
    def __init__(self, configuration, file, db_conf = None):
        self.db_conf = db_conf
        self.file = file
        self.configuration = configuration
        self.model = getattr(importlib.import_module("src.modelProcessing.modelAlgorithms.algorithms"), configuration.get_entry('modelAlgorithm'))(configuration)

    def process(self, data_map):
        self.model.setup(data_map)
        self.file.write("model algorithm: " + str(self.configuration.get_entry('modelAlgorithm')) + '\n')
        self.model.train()
        if self.model.learning_data is not None and self.db_conf is not None:
            print(str(self.configuration.config))
            plot_learning_curve(self.model.learning_data, str(self.configuration.get_entry('modelAlgorithm')), str(self.db_conf.get_entry(DataLoadingConfigurationEntries.DATA_FILEPATH.value)))
        return DataFrame(self.model.predict(), columns=None)


