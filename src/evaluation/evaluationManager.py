import importlib
import sys

from src.common.configuration.conf import EvaluationConfigurationEntries
from src.common.results import Results


class EvaluationManager:
    def __init__(self, configuration, file):
        self.metrics = []
        self.metric_names = configuration.get_entry(EvaluationConfigurationEntries.METRICS.value)
        self.file = file
        for m in range(len(self.metric_names)):
            self.metrics.append(getattr(importlib.import_module("src.evaluation.evaluationMetric.metrics"), self.metric_names[m])())

    def evaluate(self, process_result, data_map):
        results = []
        for m in range(len(self.metrics)):
            result = self.metrics[m].calculate(process_result, data_map)
            result_str = self.metric_names[m] + " = " + str(result)
            self.file.write(result_str + '\n')
            results.append(result)

        return results
