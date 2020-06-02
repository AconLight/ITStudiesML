import importlib

from pandas import DataFrame

from src.common.configuration.conf import DataLoadingConfigurationEntries
from src.data_visualization.effectiveness import plot_learning_curve
from src.data_visualization.save_matrix import save_matrix
from src.evaluation.evaluationMetric.metrics.confusion_matrix import ConfusionMatrix


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
        res = self.model.predict()
        # if "CLASSIFICATION_COLUMN_test" in data_map:
        #     save_matrix(ConfusionMatrix().calculate(res, data_map), str(self.configuration.get_entry('modelAlgorithm')), str(self.db_conf.get_entry(DataLoadingConfigurationEntries.DATA_FILEPATH.value)))

        # if "CLASSIFICATION_COLUMN_test" in data_map and self.model.learning_data is not None and self.db_conf is not None:
        #     print(str(self.configuration.config))
        #     plot_learning_curve(self.model.learning_data, str(self.configuration.get_entry('modelAlgorithm')), str(self.db_conf.get_entry(DataLoadingConfigurationEntries.DATA_FILEPATH.value)))
        return DataFrame(res, columns=None)


