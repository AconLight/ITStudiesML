import importlib

from src.common.classificationOutput import ClassificationOutput


class ModelProcessor:
    def __init__(self, conf):
        self.algorithm = getattr(importlib.import_module("src.modelProcessing.modelAlgorithms.algorithms"), conf['modelAlgorithm'])()

    def process(self, dataSet):
        classificationOutput = ClassificationOutput()

        # TODO

        return classificationOutput

