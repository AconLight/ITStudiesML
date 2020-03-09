import importlib
import sys

from src.common.results import Results


class EvaluationManager:
    def __init__(self, conf):
        self.metric = getattr(importlib.import_module("src.evaluation.evaluationMetric.metrics"), conf['evaluationMetric'])()

    def evaluate(self, classificationOutput):
        results = Results()

        # TODO

        return results
