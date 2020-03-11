import importlib
import sys

from src.common.configuration.conf import EvaluationConfigurationEntries
from src.common.results import Results


class EvaluationManager:
    def __init__(self, configuration):
        self.metric = getattr(importlib.import_module("src.evaluation.evaluationMetric.metrics"), configuration.get_entry(EvaluationConfigurationEntries.METRICS))()

    def evaluate(self, Y_pred, Y_test):
        results = Results()

        # TODO

        return results
