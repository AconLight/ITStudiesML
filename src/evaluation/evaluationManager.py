import importlib
import sys

from src.common.configuration.conf import EvaluationConfigurationEntries
from src.common.results import Results


class EvaluationManager:
    def __init__(self, configuration):
        self.metrics = []
        self.metric_names = configuration.get_entry(EvaluationConfigurationEntries.METRICS.value)
        for m in range(len(self.metric_names)):
            self.metrics.append(getattr(importlib.import_module("src.evaluation.evaluationMetric.metrics"), self.metric_names[m])())

    def evaluate(self, Y_pred, Y_test):
        results = Results()

        for m in range(len(self.metrics)):
            print(self.metric_names[m] + " = " + str(self.metrics[m].calculate(Y_pred, Y_test)))


        # TODO show results

        return results
